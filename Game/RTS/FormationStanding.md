using Unity.Entities;
using Unity.Mathematics;
using Unity.Collections;

public struct NavigationTarget : IComponentData
{
    public float3 Value;
}

public struct BoxColliderSize : IComponentData
{
    public float3 Size;
}

public partial struct FormationSystem : ISystem
{
    public void OnUpdate(ref SystemState state)
    {
        EntityQuery query = SystemAPI.QueryBuilder()
            .WithAll<BoxColliderSize, LocalTransform, NavigationTarget>()
            .Build();

        int count = query.CalculateEntityCount();
        if (count == 0) return;

        // 获取所有单位的 boxCollider 尺寸和位置
        NativeArray<Entity> entities = query.ToEntityArray(Allocator.Temp);
        NativeArray<float3> sizes = query.ToComponentDataArray<BoxColliderSize, float3>(Allocator.Temp);
        NativeArray<float3> positions = query.ToComponentDataArray<LocalTransform, float3>(Allocator.Temp);
        float3 targetPosition = new float3(0, 0, 0); // 你可以设定目标点

        // 计算每个单位的近似半径
        NativeArray<float> radii = new NativeArray<float>(count, Allocator.Temp);
        for (int i = 0; i < count; i++)
        {
            float3 size = sizes[i];
            radii[i] = math.length(size) * 0.5f; // 近似半径
        }

        // 计算单位的站位点
        NativeArray<float3> newPositions = ComputeFormationPositions(targetPosition, radii, count, Allocator.Temp);

        // 设置新目标位置
        for (int i = 0; i < count; i++)
        {
            state.EntityManager.SetComponentData(entities[i], new NavigationTarget { Value = newPositions[i] });
        }

        entities.Dispose();
        sizes.Dispose();
        positions.Dispose();
        radii.Dispose();
        newPositions.Dispose();
    }

    /// <summary>
    /// 计算单位的非重叠目标站位
    /// </summary>
    private static NativeArray<float3> ComputeFormationPositions(float3 target, NativeArray<float> radii, int count, Allocator allocator)
    {
        NativeArray<float3> positions = new NativeArray<float3>(count, allocator);
        float spacing = math.cmax(radii) * 2.0f; // 基于最大单位尺寸的间距

        int sqrtCount = (int)math.ceil(math.sqrt(count));
        int index = 0;

        // 生成网格状站位
        for (int x = -sqrtCount / 2; x <= sqrtCount / 2; x++)
        {
            for (int z = -sqrtCount / 2; z <= sqrtCount / 2; z++)
            {
                if (index >= count) break;
                positions[index] = target + new float3(x * spacing, 0, z * spacing);
                index++;
            }
            if (index >= count) break;
        }
        return positions;
    }
}


以下是基于Unity ECS和Mathematics库实现的代码，用于根据单位体积自动分配目标位置，避免重叠：

```csharp
using Unity.Collections;
using Unity.Entities;
using Unity.Mathematics;
using Unity.Transforms;
using UnityEngine;
using Unity.Physics;

// 标记组件，触发重新分配位置
public struct RepositionUnitsCommand : IComponentData
{
    public float3 TargetCenter;
}

// 单位导航组件（示例，根据实际实现调整）
public struct NavAgent : IComponentData
{
    public float3 TargetPosition;
}

[UpdateInGroup(typeof(SimulationSystemGroup))]
public partial class UnitRepositionSystem : SystemBase
{
    private EntityQuery _unitQuery;

    protected override void OnCreate()
    {
        base.OnCreate();
        _unitQuery = GetEntityQuery(
            ComponentType.ReadOnly<BoxCollider>(),
            ComponentType.ReadWrite<NavAgent>()
        );
        RequireForUpdate<RepositionUnitsCommand>();
    }

    private struct UnitData
    {
        public Entity Entity;
        public float Radius;
    }

    protected override void OnUpdate()
    {
        if (!SystemAPI.TryGetSingletonEntity<RepositionUnitsCommand>(out var cmdEntity))
            return;

        var cmd = EntityManager.GetComponentData<RepositionUnitsCommand>(cmdEntity);
        EntityManager.DestroyEntity(cmdEntity);

        using var entities = _unitQuery.ToEntityArray(Allocator.Temp);
        using var colliders = _unitQuery.ToComponentDataArray<BoxCollider>(Allocator.Temp);

        if (entities.Length == 0) return;

        // 收集单位数据
        var units = new NativeList<UnitData>(Allocator.Temp);
        foreach (var (entity, collider) in entities.Zip(colliders))
        {
            var halfSize = collider.Size;
            units.Add(new UnitData
            {
                Entity = entity,
                Radius = math.max(halfSize.x, halfSize.z) // 使用半轴长度作为半径
            });
        }

        // 按半径降序排序
        units.Sort((a, b) => b.Radius.CompareTo(a.Radius));

        int count = units.Length;
        float requiredRadius = 0f;

        if (count > 1)
        {
            // 计算最大相邻半径和
            float maxSum = 0;
            for (int i = 0; i < count; i++)
            {
                int next = (i + 1) % count;
                float sum = units[i].Radius + units[next].Radius;
                maxSum = math.max(maxSum, sum);
            }

            // 计算所需半径
            float angleStep = math.PI / count;
            float sinTerm = math.sin(angleStep);
            requiredRadius = maxSum / (2 * sinTerm);
        }

        // 分配位置
        float angleIncrement = (2f * math.PI) / count;
        for (int i = 0; i < count; i++)
        {
            float angle = i * angleIncrement;
            float3 offset = new float3(math.cos(angle), 0, math.sin(angle)) * requiredRadius;
            
            var agent = EntityManager.GetComponentData<NavAgent>(units[i].Entity);
            agent.TargetPosition = cmd.TargetCenter + offset;
            EntityManager.SetComponentData(units[i].Entity, agent);
        }

        units.Dispose();
    }
}
```

实现说明：

1. **组件结构**：
   - `RepositionUnitsCommand`：触发位置重分配的标记组件
   - `NavAgent`：自定义导航组件，需包含目标位置字段
   - `BoxCollider`：使用Unity Physics的碰撞体组件

2. **核心算法**：
   - 按碰撞体半径降序排列单位
   - 计算保证相邻单位不重叠的最小圆周半径
   - 使用极坐标均匀分配位置

3. **半径计算**：
   ```csharp
   Radius = math.max(halfSize.x, halfSize.z)
   ```
   使用BoxCollider在XZ平面的最大半轴长度作为半径

4. **安全距离计算**：
   ```csharp
   requiredRadius = maxSum / (2 * math.sin(math.PI / count))
   ```
   确保相邻单位保持最小安全距离

5. **位置分配**：
   ```csharp
   float3 offset = new float3(math.cos(angle), 0, math.sin(angle)) * requiredRadius
   ```
   使用极坐标转换到目标点周围

使用方式：

1. 为需要重新定位的单位添加`BoxCollider`和`NavAgent`组件
2. 创建包含`RepositionUnitsCommand`组件的实体来触发分配
3. 系统会自动计算并更新所有单位的`NavAgent.TargetPosition`

优化建议：

1. 对于动态更新需求，可以添加重分配间隔控制
2. 结合空间划分算法优化大规模单位定位
3. 添加高度（Y轴）维度处理3D空间定位
4. 使用JobSystem并行化计算过程

注意：实际使用时需根据具体导航系统实现调整`NavAgent`组件的字段和更新逻辑。