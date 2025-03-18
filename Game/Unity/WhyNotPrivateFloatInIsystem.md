**核心问题：为什么 `float` 不能存，但 `NativeArray<float>` 可以？**  

---

### **1. `ISystem` 是 `struct`，所有字段默认在 `Burst` 运行**
`ISystem` 是一个 `struct`，如果你直接在 `ISystem` 里声明 `private float myValue;`，这个 `float` **会在 `Burst` 编译时被 `zero-initialized`（默认为 0）**，导致它无法保持状态。  

但 `NativeArray<T>` 是一个**托管的 `struct`，内部有指针指向 `Native` 内存区域**，即使 `ISystem` 被复制，它仍然可以保持数据不丢失。

---

### **2. `float` 是值类型，存 `ISystem` 会丢失状态**
```csharp
public struct MySystem : ISystem
{
    private float myValue; // ❌ 这个值在每次 `OnUpdate` 可能被重置

    public void OnUpdate(ref SystemState state)
    {
        myValue += 1; // 这里的 `myValue` 可能在下一帧又变回 0
        UnityEngine.Debug.Log(myValue);
    }
}
```
- 由于 `ISystem` 由 `Burst` 管理，每次 `OnUpdate` 可能会使用一个新的 `MySystem` 结构，导致 `myValue` **每帧重置**。
- 这与 `SystemBase`（class 继承）不同，`SystemBase` 作为 `class` 是持久化对象，`float` 变量可以正常存储状态。

---

### **3. `NativeArray<float>` 是托管的 `struct`，不会被 `ISystem` 复制**
```csharp
public struct MySystem : ISystem
{
    private NativeArray<float> myArray;

    public void OnCreate(ref SystemState state)
    {
        myArray = new NativeArray<float>(1, Allocator.Persistent);
    }

    public void OnUpdate(ref SystemState state)
    {
        myArray[0] += 1;
        UnityEngine.Debug.Log(myArray[0]); // ✅ 这个值可以保持累加
    }

    public void OnDestroy(ref SystemState state)
    {
        if (myArray.IsCreated)
            myArray.Dispose();
    }
}
```
- `NativeArray<T>` **底层存储在 `Native` 内存**，即使 `ISystem` 结构体被复制，指向 `Native` 内存的指针不会变。
- **只要 `NativeArray<T>` 没有被 `Dispose()`，数据不会丢失**。

---

### **结论**
| 变量类型 | 存储在 `ISystem` 里 | 能否持久化 | 备注 |
|----------|----------------|----------|------|
| `float`  | ❌ 不推荐 | ❌ **会重置** | `struct` 复制导致数据丢失 |
| `NativeArray<float>` | ✅ **可以** | ✅ **数据不会丢失** | `NativeArray` 存在 `Native` 内存 |
| `float` 存在 `Component` | ✅ **推荐** | ✅ **数据不会丢失** | 存到 `Singleton` 或 `IComponentData` |
| `SystemBase` 里的 `float` | ✅ **可以** | ✅ **数据不会丢失** | `SystemBase` 是 `class`，不会被复制 |

---

### **最佳实践**
如果你需要存**全局配置（不变的值）**：
- **存入 `SingletonComponent`**，然后 `GetSingleton<ConfigData>()` 获取。

如果你需要存**可变状态（比如计时器、配置数据）**：
- **用 `NativeArray<float>` 存在 `ISystem` 内**，但需要 `OnDestroy` 释放。

如果你只需要**在 `OnUpdate` 临时使用**：
- **直接 `float myValue = GetSingleton<ConfigData>().myFloat;`，不需要存 `ISystem` 内**。

---

所以：
✅ **`float` 不能直接存，但 `NativeArray<float>` 可以**，因为 `NativeArray` 不受 `struct` 复制影响，数据持久化在 `Native` 内存！