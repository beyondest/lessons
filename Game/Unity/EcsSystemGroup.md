## **1️⃣ ECS 中的 `SystemGroup` 结构**
Unity ECS（DOTS）的 `SystemGroup` 控制 `System` 的 **执行顺序**，分为多个主要的 `SystemGroup`，按照 **帧更新（Frame Update）** 依次执行。  

---

## **2️⃣ ECS `SystemGroup` 的执行顺序**
ECS `SystemGroup` 的执行顺序如下（**从上到下依次执行**）：  

### **🚀 `InitializationSystemGroup`（初始化组）**
| **时间点** | **系统名称** | **作用** |
|------------|-------------|-------------|
| **帧开始** | `InitializationSystemGroup` | 处理 **游戏逻辑初始化**、**事件重置**、**前一帧数据清理** |
| 🏷 **子组** | `BeginSimulationEntityCommandBufferSystem` | 用于安全地修改 `Entity`（**创建/销毁**）|
| 🏷 **子组** | `TransformSystemGroup` | 更新 `LocalToWorld`、`Parent` 变换关系 |

✅ **适用于**
- 初始化数据（例如重置 `Cooldown` 时间、设置 `状态机`）。
- 处理 **`Entity` 添加/移除组件**（通常使用 `EntityCommandBufferSystem`）。

---

### **🎮 `SimulationSystemGroup`（模拟系统组）**
| **时间点** | **系统名称** | **作用** |
|------------|-------------|-------------|
| **物理前** | `FixedStepSimulationSystemGroup` | 用于**物理计算**（`FixedUpdate()` 逻辑） |
| **主要执行** | `SimulationSystemGroup` | **核心游戏逻辑（Gameplay）** |
| 🏷 **子组** | `PhysicsSystemGroup` | 处理 **Unity Physics 物理系统** |
| 🏷 **子组** | `LateSimulationSystemGroup` | 处理 **延迟模拟（如 Buff 结算、动画）** |
| 🏷 **子组** | `EndSimulationEntityCommandBufferSystem` | 用于安全地**修改 `Entity`（销毁/修改）** |

✅ **适用于**
- **游戏主要逻辑**（角色 AI、战斗、资源采集等）。
- **物理运算（Unity Physics）**。
- **处理 Buff、冷却时间、技能结算**。

---

### **🎨 `PresentationSystemGroup`（渲染系统组）**
| **时间点** | **系统名称** | **作用** |
|------------|-------------|-------------|
| **渲染前** | `PresentationSystemGroup` | 处理 **UI 更新、动画、音效** |
| 🏷 **子组** | `LateSimulationSystemGroup` | 确保游戏逻辑完成后再更新动画 |
| 🏷 **子组** | `RenderingSystemGroup` | 控制 **MeshRenderer、Material** 等渲染数据 |

✅ **适用于**
- **UI 逻辑（血条、得分、伤害数值）**。
- **处理 `Animator` 组件**。
- **音效播放、摄像机逻辑**。

---

### **🔄 `LateSimulationSystemGroup`（延迟模拟组）**
这个 `SystemGroup` **在 `SimulationSystemGroup` 之后执行**，用于：
- **结算 Buff、生存检测（如死亡单位移除）**。
- **同步 UI 组件，如 `HealthBar` 绑定 `Health` 组件**。

---

## **3️⃣ 自定义 `ISystem` 和 `SystemBase` 应该放在哪？**
| **系统类型** | **推荐 `SystemGroup`** | **适用场景** |
|-------------|----------------------|-------------|
| **初始化逻辑（初始化组件、事件重置）** | `InitializationSystemGroup` | 重置冷却、初始化状态 |
| **主游戏逻辑（战斗、AI、交互）** | `SimulationSystemGroup` | 主要 Gameplay 逻辑 |
| **物理运算（碰撞、速度计算）** | `PhysicsSystemGroup` | 使用 Unity Physics |
| **UI 逻辑（同步血量、经验条）** | `PresentationSystemGroup` | 更新 UI、动画、音效 |
| **延迟处理（死亡移除、战斗结算）** | `LateSimulationSystemGroup` | 结算 Buff、角色死亡检测 |

### **📌 如何在 `ISystem` / `SystemBase` 指定 `SystemGroup`**
**✅ `ISystem` 版本**
```csharp
[UpdateInGroup(typeof(SimulationSystemGroup))] // 设定系统在游戏逻辑执行
public partial struct MyGameSystem : ISystem
{
    public void OnUpdate(ref SystemState state)
    {
        // 处理游戏逻辑
    }
}
```

**✅ `SystemBase` 版本**
```csharp
[UpdateInGroup(typeof(PresentationSystemGroup))] // 设定 UI 更新
public partial class MyUISystem : SystemBase
{
    protected override void OnUpdate()
    {
        // 更新 UI
    }
}
```

---

## **4️⃣ `SystemGroup` 执行顺序总结**
```
1. InitializationSystemGroup  (初始化)
    - BeginSimulationEntityCommandBufferSystem（处理 Entity 创建/删除）
    - TransformSystemGroup（更新 `LocalToWorld`）

2. SimulationSystemGroup  (游戏逻辑)
    - FixedStepSimulationSystemGroup（物理计算，类似 `FixedUpdate()`）
    - PhysicsSystemGroup（物理系统）
    - LateSimulationSystemGroup（Buff、状态结算）
    - EndSimulationEntityCommandBufferSystem（销毁 `Entity`）

3. PresentationSystemGroup  (渲染/UI)
    - RenderingSystemGroup（Mesh、动画、UI 更新）
```

---

## **5️⃣ 结论**
💡 **如果你的 `System` 处理游戏逻辑（战斗、AI、技能），就放在 `SimulationSystemGroup`。**  
💡 **如果你的 `System` 需要操作 `Entity`（创建/删除），请用 `BeginSimulationEntityCommandBufferSystem` 或 `EndSimulationEntityCommandBufferSystem`。**  
💡 **如果你的 `System` 处理 UI、动画、音效，放在 `PresentationSystemGroup`。**  

🚀 这样，你的 ECS `System` 就能按照**最优的执行顺序运行，避免逻辑错误**！




在 **Unity ECS Hybrid（即同时使用 ECS 和 `MonoBehaviour`）** 的情况下，ECS `System` 的 `Update` 时间和 `MonoBehaviour` 的 `Update` 顺序可以通过以下方式判断和控制：

---

## **1. ECS `System` 和 `MonoBehaviour` 的 `Update` 顺序**
在 Unity 的 `PlayerLoop` 事件中，**ECS `System` 默认是在 `Update` 阶段执行的**，但具体顺序取决于它所在的 `SystemGroup`。

Unity 的 `PlayerLoop` 执行顺序如下：
```
Initialization
    ├── EarlyUpdate
    ├── FixedUpdate
    ├── PreUpdate
    ├── Update
        ├── MonoBehaviour.Update() (所有 MonoBehaviour Update)
        ├── SimulationSystemGroup (ECS 默认系统组)
        ├── PresentationSystemGroup (渲染相关 ECS 系统)
    ├── PreLateUpdate
    ├── PostLateUpdate
```
**默认情况下：**
- **所有 `MonoBehaviour.Update()` 在 `SimulationSystemGroup` 之前执行**
- **ECS `SystemBase` 主要在 `SimulationSystemGroup` 中运行**
- **ECS 依赖 `JobHandle`，如果 `System` 里有 `Job`，它可能会跨多个帧并行执行**

---

## **2. 如何判断 ECS `System` 和 `MonoBehaviour` 的 `Update` 先后**
你可以通过 **`Debug.Log()`** 在 `MonoBehaviour` 和 `SystemBase` 里打印帧时间来检查：
```csharp
public class MyMono : MonoBehaviour
{
    void Update()
    {
        Debug.Log($"MonoBehaviour.Update() at {Time.frameCount}");
    }
}
```
```csharp
public partial class MyECSSystem : SystemBase
{
    protected override void OnUpdate()
    {
        Debug.Log($"ECS SystemBase.OnUpdate() at {Time.frameCount}");
    }
}
```
**结果**
如果你运行代码，通常会发现：
```
MonoBehaviour.Update() at 1
ECS SystemBase.OnUpdate() at 1
MonoBehaviour.Update() at 2
ECS SystemBase.OnUpdate() at 2
```
这说明 **默认情况下 `MonoBehaviour.Update()` 先执行，然后 ECS `System` 执行**。

---

## **3. 如何控制 `System` 的执行顺序**
如果你希望 **ECS `System` 在 `MonoBehaviour` 之前执行或之后执行**，你可以修改 `System` 的 `Update` 时机。

### **方法 1：让 `System` 在 `MonoBehaviour` 之前执行**
- 让 `System` 进入 **`PreUpdate` 阶段**（在 `MonoBehaviour.Update()` 之前）
- 通过 `World.GetOrCreateSystem<UpdateBeforeSimulationGroup>()` 重新注册 `System`

示例：
```csharp
[UpdateInGroup(typeof(PreUpdate))]
public partial class MyECSSystem : SystemBase
{
    protected override void OnUpdate()
    {
        Debug.Log("ECS System running before MonoBehaviour Update.");
    }
}
```
✅ **这样 `ECS System` 会在 `MonoBehaviour.Update()` 之前运行！**

---

### **方法 2：让 `System` 在 `MonoBehaviour` 之后执行**
如果你希望 `System` 在 `MonoBehaviour` 之后执行：
- 让 `System` 进入 `PostLateUpdate`（MonoBehaviour `LateUpdate()` 之后）

```csharp
[UpdateInGroup(typeof(PostLateUpdate))]
public partial class MyECSSystem : SystemBase
{
    protected override void OnUpdate()
    {
        Debug.Log("ECS System running after MonoBehaviour Update.");
    }
}
```
✅ **这样 `ECS System` 会在 `MonoBehaviour.Update()` 之后运行。**

---

## **4. 如何让 `MonoBehaviour` 在 ECS `System` 运行后执行**
有时候，你可能希望 `MonoBehaviour` 读取 `ECS` 计算后的数据，例如：
- **ECS 计算物理模拟**
- **MonoBehaviour 读取 ECS 结果来更新 UI**

### **方法 1：在 `LateUpdate()` 读取 ECS 计算结果**
`LateUpdate()` **默认在 ECS 之后执行**，可以安全地读取 `ECS` 计算的数据：
```csharp
public class MyMono : MonoBehaviour
{
    void LateUpdate()
    {
        Debug.Log("MonoBehaviour LateUpdate() reading ECS data.");
    }
}
```

### **方法 2：使用 `SystemBase.CompleteDependency()`**
如果 `MonoBehaviour` 需要立即读取 `ECS` 计算结果，而不等到 `LateUpdate()`：
```csharp
public partial class MyECSSystem : SystemBase
{
    protected override void OnUpdate()
    {
        JobHandle job = Entities
            .ForEach((ref LocalTransform transform) =>
            {
                transform.Position += new float3(1, 0, 0);
            }).ScheduleParallel(Dependency);

        job.Complete(); // 确保所有 Job 完成
    }
}
```
然后 `MonoBehaviour` **在同一帧中可以立即读取 ECS 计算结果**。

---

## **5. 总结**
| 需求 | 解决方案 |
|------|---------|
| **ECS `System` 先执行，MonoBehaviour `Update` 后执行** | `PreUpdate` |
| **MonoBehaviour `Update` 先执行，ECS `System` 后执行** | 默认 `Update` 顺序 |
| **ECS `System` 计算后，MonoBehaviour 读取数据** | `LateUpdate()` or `CompleteDependency()` |

🔹 **默认情况下，`MonoBehaviour.Update()` 先执行，ECS `SystemBase` 后执行。**  
🔹 **如果要改变顺序，可以用 `UpdateInGroup(typeof(PreUpdate))` 或 `PostLateUpdate`。**  
🔹 **如果 `MonoBehaviour` 需要用 ECS 计算的数据，可以 `LateUpdate()` 或 `CompleteDependency()`。**

这样就可以在 Hybrid 模式下控制 `MonoBehaviour` 和 `ECS` `System` 的执行顺序了！🚀