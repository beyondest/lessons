### **📌 为什么 `+=` 订阅事件要放在 `OnEnable()` 而不是 `Start()` 或 `Awake()`？**

🔹 **核心原因：保证事件监听的动态管理**  
🔹 **防止潜在的空引用错误**  
🔹 **确保在 `GameObject` 被禁用/启用时，事件可以正确移除/恢复**

---

### **📍 `OnEnable()` vs `Start()` vs `Awake()`**
| 方法 | 触发时机 | 适用于 |
|------|---------|------|
| **`Awake()`** | 在 `Start()` **之前** 调用（对象初始化） | 初始化变量、加载资源，但此时 `ClickManager.Instance` 可能还未创建 |
| **`Start()`** | 在 `Awake()` 之后，**第一帧** 运行时调用 | 适用于使用 `Instance` 获取组件的情况 |
| **`OnEnable()`** | **每次对象被启用时** 调用 | **事件订阅，确保启用时能正确触发** |

---

### **📌 为什么 `OnEnable()` 适合订阅事件？**
#### **✅ 1. 确保禁用再启用时能恢复监听**
- **`Start()` 只会在 `GameObject` **第一次** 启用时执行**，如果你在 `Start()` 里订阅了 `ClickManager.Instance.OnClickObject`：
  - 之后你 `SetActive(false)` 再 `SetActive(true)`，**事件不会自动重新订阅！**
  - 这样 `ClickManager` 触发 `OnClickObject.Invoke()` 时，你的 `SelectUnit()` 方法不会执行了。

**而 `OnEnable()` 每次启用都会执行**，可以重新订阅事件，保证正常工作。

```csharp
private void OnEnable()
{
    ClickManager.Instance.OnClickObject += SelectUnit;
}

private void OnDisable()
{
    ClickManager.Instance.OnClickObject -= SelectUnit;
}
```
- 当 `GameObject` 重新 `SetActive(true)` 时，`OnEnable()` 重新订阅事件，确保点击事件仍然能触发 `SelectUnit()`。

---

#### **✅ 2. 防止 `NullReferenceException`**
**如果 `ClickManager.Instance` 还没初始化（比如在 `Awake()` 执行时）**，你在 `Awake()` 或 `Start()` 里直接订阅可能会导致 `NullReferenceException`。

而 `OnEnable()` 执行时，`ClickManager.Instance` **通常已经完成初始化**，避免了这个问题。

---

#### **✅ 3. 解除订阅，防止事件泄漏**
如果不在 `OnDisable()` 里 `-=` 取消订阅，**当 GameObject 被销毁时，事件仍然会持有它的引用**，导致：
- **内存泄漏**（对象无法被 GC 释放）
- **调用已经被销毁的对象，触发 `NullReferenceException`**

通过 `OnDisable()` 解除订阅，可以防止这个问题：
```csharp
private void OnDisable()
{
    ClickManager.Instance.OnClickObject -= SelectUnit;
}
```

---

### **📌 什么时候 `Start()` 适合订阅事件？**
如果 **GameObject 不会被 SetActive(false)/SetActive(true) 切换**，你也可以在 `Start()` 里订阅事件：
```csharp
private void Start()
{
    ClickManager.Instance.OnClickObject += SelectUnit;
}
```
但这不适用于 **可动态启用/禁用的 UI、单位、物品等对象**。

---

### **📌 什么时候 `Awake()` 适合订阅事件？**
**如果你能 100% 确保事件管理器（`ClickManager.Instance`）在 `Awake()` 之前就已经初始化**，可以在 `Awake()` 里订阅：
```csharp
private void Awake()
{
    ClickManager.Instance.OnClickObject += SelectUnit;
}
```
但如果 `ClickManager` 还没初始化，这样会导致 `NullReferenceException`。

**所以推荐 `OnEnable()`，更安全、更适用于可动态启用/禁用的对象！** 🚀