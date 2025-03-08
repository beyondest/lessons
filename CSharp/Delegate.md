在这行代码中：  
```csharp
public event Action<string> OnSceneLoaded = delegate { };
```
`delegate { };` 是**匿名方法**（Anonymous Method），这里它的作用是**给 `OnSceneLoaded` 事件赋一个默认的空委托，防止 `Invoke` 时空引用**。

---

## **📌 `delegate { };` 的作用**
通常，我们在 `Invoke` 事件时，需要确保它不为空。例如：
```csharp
OnSceneLoaded?.Invoke("MainScene"); // 如果 OnSceneLoaded 是 null，会导致 NullReferenceException
```
如果**没有任何订阅者**，`OnSceneLoaded` 就是 `null`，调用 `Invoke` 会报 `NullReferenceException`。  

为了避免 `null`，我们可以在声明时给它一个**默认的空委托**：
```csharp
public event Action<string> OnSceneLoaded = delegate { };
```
这样，即使没有订阅者，`OnSceneLoaded.Invoke("MainScene")` 也不会报错，因为它默认执行的是：
```csharp
delegate { }; // 什么都不做，不会抛出异常
```

---

## **💡 `delegate { };` 详解**
`delegate { };` 是 C# **匿名方法**（Anonymous Method）的简写形式，等价于：
```csharp
delegate(string sceneName) { };
```
它是一个**什么都不做的委托**，也可以写成：
```csharp
public event Action<string> OnSceneLoaded = (sceneName) => { };
```
它表示**默认情况下，这个事件执行后什么都不会发生**，但不会是 `null`，所以可以安全调用 `Invoke()`。

---

## **🔹 示例**
### **✅ 正确使用 `delegate { };`**
```csharp
public class SceneLoader
{
    // 避免 NullReferenceException
    public event Action<string> OnSceneLoaded = delegate { };

    public void LoadScene(string sceneName)
    {
        Console.WriteLine($"Loading {sceneName}...");
        
        // 这里不会报错，即使没有订阅者
        OnSceneLoaded.Invoke(sceneName);
    }
}
```
即使没有任何监听 `OnSceneLoaded`，`Invoke()` 也不会崩溃。

---

### **⛔ 错误示例：没有默认值，可能报错**
```csharp
public class SceneLoader
{
    public event Action<string> OnSceneLoaded;

    public void LoadScene(string sceneName)
    {
        Console.WriteLine($"Loading {sceneName}...");
        
        // 如果没有订阅者，OnSceneLoaded 是 null，调用 Invoke() 会崩溃
        OnSceneLoaded.Invoke(sceneName);
    }
}
```
如果 `OnSceneLoaded` 没有订阅者，这行代码：
```csharp
OnSceneLoaded.Invoke(sceneName);
```
会抛出：
```
NullReferenceException: Object reference not set to an instance of an object
```

---

## **🚀 结论**
- `delegate { };` 是**匿名方法**，相当于 `()=>{}`，表示“什么都不做”。
- 主要作用是**避免 `Invoke()` 调用空事件时报 `NullReferenceException`**。
- 适用于 `event` 事件，确保即使没有订阅者也能安全调用。

你可以放心使用这种写法，尤其是在 `event` 事件里！🚀