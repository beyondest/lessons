帮我设计一个速用，简单容易实现的敌人ai决策系统，ecs兼容，不需要给出能跑的代码，关键是实现思路和伪代码，最关键的是：datacomponent或者buffer的设计，以及system和job的设计，哪一块负责什么功能。
我的rts裂隙如前所述，是光暗对抗的人机对抗rts，并且由于时间紧迫我决定主要开发波数+rogue制，敌人以波数进攻玩家建筑，玩家需要保护中心水晶不被破坏；敌人的建筑按照波数生成，玩家破坏敌人的中心水晶该波次成功，并且一定时间后开始下一波。玩家的积分以波数累计，每波敌人会越来越多，建筑和单位都会越来越强，但是敌人建筑中会有若干个被困的强力单位，玩家解救后可以加入玩家阵营。资源以自然资源和玩家基地自己生产的资源为主，要求每波根据预先的难度设定，生成不同数量的自然资源。
我已经实现了视野target list和自动单位选择系统，所有可以成为目标的单位身上都有一个componentdata：priority，通过设置这个，可以让单位实现优先攻击目标，并且我也实现了一套寻路系统，可以让单位优先避开所有能进攻的建筑（如箭塔），并且让单位指定攻击一个被围起来的目标时，将会自动选择防御最薄弱的地方进攻。基础的ai已经实现，现在缺的是大方向的




这类波数 + Rogue 机制 RTS 游戏的敌人 AI 可以设计得轻量却具有可扩展性，以下是一个 **ECS 兼容、易实现并符合你已有系统的 AI 决策系统设计方案**。

---

## 🎯 目标

构建一个大方向敌人 AI 框架，控制敌人：
1. 按波次决定“建什么”、“派谁出击”、“在哪建”、“攻哪打”；
2. 根据玩家状态与既定策略调整行动优先级；
3. 系统分工清晰、DataComponent 可调、系统可拓展。

---

## 🧩 Component 和 Buffer 设计

### 📌 1. `EnemyWaveTag`（IComponentData）  
标记当前属于某一波的单位或建筑，用于分波管理。

### 📌 2. `EnemyAICommandBuffer`（IBufferElementData）  
敌人执行计划队列（类似 BT 中的节点）：

```csharp
public struct EnemyAICommand : IBufferElementData
{
    public AICommandType CommandType;  // 建造、进攻、采集等
    public Entity TargetEntity;
    public float ExecuteTime;
    public float Priority;
}

public enum AICommandType
{
    Build,
    Attack,
    Defend,
    Retreat,
    Patrol,
    Gather
}
```

### 📌 3. `EnemyAIState`（IComponentData）  
敌人的当前状态，用于控制是否能执行某些命令：

```csharp
public struct EnemyAIState : IComponentData
{
    public AIStateType CurrentState; // Idle, Attacking, Retreating
    public float StateTime;
}
```

### 📌 4. `EnemyAIBrain`（IComponentData）  
代表敌方“指挥官”的实体数据，只有一个，用于管理决策：

```csharp
public struct EnemyAIBrain : IComponentData
{
    public int CurrentWave;
    public float TimeSinceLastWave;
    public float NextWaveCooldown;
    public float CurrentDifficulty;
}
```

### 📌 5. `EnemySpawnRequest`（IComponentData）  
用于波次生成敌人建筑或单位的数据结构：

```csharp
public struct EnemySpawnRequest : IComponentData
{
    public Entity Prefab;
    public float3 Position;
    public int Tier;
    public float Delay; // 延迟生成时间
}
```

---

## ⚙️ System 分工设计

### 1. `EnemyWaveControlSystem`  
- 负责监控 `EnemyAIBrain` 中的时间与波次；
- 如果时间到 -> 增加波次 + 生成新的 `EnemySpawnRequest`；
- 增加自然资源实体到随机区域（用 `WaveSpawnRegion` Component）；
- 提高难度（如敌人单位 Tier、数量等）；
- ✅ 运行在主线程，或部分 Job 化。

---

### 2. `EnemySpawnSystem`  
- 扫描所有 `EnemySpawnRequest`，到时间后在指定位置生成单位或建筑；
- 使用 CommandBuffer 实现异步生成；
- ✅ Job 化处理生成与摆放逻辑。

---

### 3. `EnemyAIPlanningSystem`  
- 由 `EnemyAIBrain` 负责分析场上局势（已有单位、玩家防御强度）；
- 向所有敌人填充 `EnemyAICommandBuffer`：
  - 攻击最近玩家水晶或最薄弱建筑；
  - 建造防御塔或兵营；
  - 解救强力中立单位；
- ✅ 可选 Job 化，如果逻辑不复杂可主线程运行。

---

### 4. `EnemyAIExecutionSystem`  
- 扫描所有敌人单位，如果有 `EnemyAICommandBuffer`，根据优先级执行首条命令；
- 例如 Attack 指令 -> 设置目标并启动移动系统；
- 执行完成后 Pop Buffer；
- ✅ Job 化。

---

### 5. `EnemyFallbackSystem`（可选）  
- 如果敌人单位闲置超过一定时间，自动执行巡逻、防守、造兵等 fallback 行为；
- 适合处理场上单位分布不均时的自动适应。

---

## 💡 示例伪代码（AI 决策）

```csharp
if (PlayerCrystalWeaklyDefended)
    Plan.Add(new EnemyAICommand { CommandType = Attack, Target = PlayerCrystal });
else if (PlayerLeftSideTowers < RightSide)
    Plan.Add(new EnemyAICommand { CommandType = Attack, Target = LeftWall });
else
    Plan.Add(new EnemyAICommand { CommandType = Build, Target = EnemyBarrackPosition });
```

---

## 🔁 数据流逻辑

1. `EnemyWaveControlSystem`：开始一波；
2. `EnemySpawnSystem`：生成敌人；
3. `EnemyAIPlanningSystem`：生成战术计划；
4. `EnemyAIExecutionSystem`：各个敌人执行各自的命令；
5. 玩家破坏敌人水晶 -> `EnemyWaveControlSystem` 标记当前波完成，准备下一波。

---

## ✅ 特点总结

- **模块独立**，可调试性强；
- **兼容ECS**，Job 易并行化；
- **快速扩展**，支持加入更多策略；
- **支持 Rogue 机制**，每波策略不同；
- **可调节敌人智能程度**，只需切换 `EnemyAIBrain` 策略模式。

---

如果你希望我补一个视觉化的 AI Debug 工具或模拟一个关卡配置器（如 ScriptableObject 设定每波敌人），我也可以帮你做。你对这个 AI 架构还有什么想法或额外需求吗？