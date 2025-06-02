你提到的是 Unity ECS 中 **系统初始化顺序** 和 **初始化逻辑应该放在哪** 这个非常典型的架构设计问题。在 RTS 这种复杂游戏里，初始化顺序对系统健壮性非常关键。

我来分部分解答你的问题：

---

## ✅ `OnCreate` 的调用顺序是否有组织？

是的：

### ✔ 所有系统的 `OnCreate()` 调用：

- 是在 **World 创建并添加系统时立即调用**，而不是按 `Update` 顺序执行。
- 系统属于某个 **SystemGroup**（如 `SimulationSystemGroup`），但 **`OnCreate()` 不受组内 Update 顺序影响**。

💡 所以：

> `OnCreate()` 的调用顺序 ≠ `UpdateInGroup/UpdateBefore/After` 所定义的顺序。

Unity 并不会自动按 Update 顺序安排 `OnCreate()` 的先后。

---

## ✅ 能否在另一个系统的 `OnCreate()` 中访问 singleton？

可以，但要谨慎。

你提到：

> 有个 GeneralInitSystem 在 `OnCreate()` 中创建 GeneralRandom 的 Singleton，另一个系统希望在它的 `OnCreate()` 里获取它。

这 **不一定安全**，除非你明确控制 `OnCreate()` 的执行顺序——但这并不是 Unity 默认支持的功能。

---

### ❌ 你不能完全控制 `OnCreate` 顺序。

比如你这样写：

```csharp
[UpdateBefore(typeof(EnemySystem))]
public partial class GeneralInitSystem : SystemBase
{
    protected override void OnCreate()
    {
        EntityManager.CreateSingleton(new GeneralRandom(...));
    }
}
```

虽然设置了 `UpdateBefore`，但：
> 这只影响 Update 顺序，不保证 `GeneralInitSystem.OnCreate()` 一定在 `EnemySystem.OnCreate()` 之前被调用。

所以你在 `EnemySystem.OnCreate()` 中访问 `GeneralRandom` 是 **不安全的** —— 它可能还不存在。

---

## ✅ 正确做法建议：

### ✅ 做法一：在 `OnUpdate()` 中延迟初始化（推荐做法）

```csharp
bool _initialized = false;

protected override void OnUpdate()
{
    if (_initialized) return;

    if (!SystemAPI.HasSingleton<GeneralRandom>())
        return;

    var genRnd = SystemAPI.GetSingleton<GeneralRandom>();
    var mySeed = genRnd.Random.NextInt();

    var enemyRnd = new EnemyRandom { Random = new Unity.Mathematics.Random((uint)mySeed) };
    EntityManager.CreateSingleton(enemyRnd);

    _initialized = true;
}
```

> ✔ 这种结构是 **安全、清晰、兼容 JobSystem 的 ECS 风格**。

你可以在 `GeneralInitSystem` 创建 `GeneralRandom` 后，`EnemySystem` 自己在第一次 Update 时完成初始化。

#### 关于你说的这个判断：

```csharp
if (!initialized && resourceReady) then init;
```

这类判断在系统第一次几帧中会有一些分支判断，但：
- 性能开销 **极小可忽略**；
- 一旦 `_initialized = true`，分支直接跳过；
- 它是 **ECS 推荐的延迟初始化方式**。

---

### ✅ 做法二：集中初始化系统（更明确但耦合更强）

你可以做一个 `InitSystem` 专门做初始化：

```csharp
[UpdateInGroup(typeof(InitializationSystemGroup))]
public partial class RTSInitSystem : SystemBase
{
    protected override void OnUpdate()
    {
        if (initDone) return;

        // 1. 创建 GeneralRandom
        EntityManager.CreateSingleton(new GeneralRandom(...));

        // 2. 创建 EnemyRandom
        var seed = SystemAPI.GetSingleton<GeneralRandom>().Random.NextInt();
        EntityManager.CreateSingleton(new EnemyRandom { Random = new Random((uint)seed) });

        initDone = true;
    }
}
```

这样做能将所有初始化集中控制，**初始化顺序可控，但系统解耦性稍差**。

---

## ✅ 结论

| 你要做的事 | 推荐方案 | 原因 |
|------------|----------|------|
| 在一个系统中创建 Singleton，另一个系统也要用 | 在 `OnUpdate()` 延迟初始化 | 安全、不会因 `OnCreate()` 顺序错误而崩溃 |
| 避免多帧判断开销 | 可以忽略 | 性能极小，对逻辑清晰帮助更大 |
| 控制初始化顺序 | 集中放在一个 InitSystem 里 | 可控、安全 |

---

### ✅ 补充建议

你也可以用 ECS 官方 `SystemState` 来辅助判断初始化是否完成（类似组件状态）：

```csharp
if (!SystemAPI.HasSingleton<EnemyRandom>())
{
    if (SystemAPI.HasSingleton<GeneralRandom>())
    {
        // 初始化并创建 EnemyRandom
    }
}
```

---

是否需要我帮你封装一个 “延迟初始化+安全判断” 的模板系统结构，适配你 RTS 的场景？