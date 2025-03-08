在 C# 中，`switch` 语句用于根据变量的值执行不同的代码块。下面是标准用法的示例：  

---

## **1. 基本 `switch` 语句**
适用于 **匹配固定值的情况**：
```csharp
public void HandleInput(char key)
{
    switch (key)
    {
        case 'W':
            Console.WriteLine("Move Up");
            break;
        case 'S':
            Console.WriteLine("Move Down");
            break;
        case 'A':
            Console.WriteLine("Move Left");
            break;
        case 'D':
            Console.WriteLine("Move Right");
            break;
        default:
            Console.WriteLine("Invalid Key");
            break;
    }
}
```
**关键点**：
- **`case` 必须使用 `break` 或 `return`**，否则会 **fall-through（贯穿执行）**。
- `default` 是可选的，但建议添加，处理未知情况。

---

## **2. `switch` 表达式（C# 8.0+ 推荐）**
适用于 **赋值的情况**，更简洁：
```csharp
public string GetDirection(char key) =>
    key switch
    {
        'W' => "Move Up",
        'S' => "Move Down",
        'A' => "Move Left",
        'D' => "Move Right",
        _   => "Invalid Key"
    };
```
✅ **优点**：
- 省略 `break`
- 更符合**函数式编程**，适用于**返回值**的情况

---

## **3. `switch` 多条件合并**
多个 `case` 执行相同逻辑：
```csharp
public void CheckVowel(char letter)
{
    switch (char.ToLower(letter))
    {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            Console.WriteLine("It's a vowel.");
            break;
        default:
            Console.WriteLine("It's a consonant.");
            break;
    }
}
```
**优点**：
- **减少重复代码**
- 适用于多个值执行相同逻辑

---

## **4. `switch` + `enum`（常见于状态机）**
适用于 **枚举类型的分支**：
```csharp
public enum GameState { MainMenu, Playing, Paused, GameOver }

public void HandleGameState(GameState state)
{
    switch (state)
    {
        case GameState.MainMenu:
            Console.WriteLine("Show Main Menu");
            break;
        case GameState.Playing:
            Console.WriteLine("Game Running...");
            break;
        case GameState.Paused:
            Console.WriteLine("Game Paused");
            break;
        case GameState.GameOver:
            Console.WriteLine("Game Over");
            break;
    }
}
```
✅ **强类型安全**，不允许传入无效值。

---

## **5. `switch` 结合 `when`（C# 7.0+）**
适用于 **复杂条件判断**：
```csharp
public string GetWeatherAdvice(int temperature)
{
    return temperature switch
    {
        <= 0 => "It's freezing! Wear a coat.",
        <= 15 => "It's chilly. Wear a jacket.",
        <= 25 => "Nice weather!",
        _ => "It's hot! Stay hydrated."
    };
}
```
也可以用于 `case`：
```csharp
public void PrintNumberType(int number)
{
    switch (number)
    {
        case int n when n < 0:
            Console.WriteLine("Negative Number");
            break;
        case int n when n > 0:
            Console.WriteLine("Positive Number");
            break;
        default:
            Console.WriteLine("Zero");
            break;
    }
}
```
✅ **比 `if-else` 结构更清晰**，适用于**模式匹配**。

---

## **6. `switch` 结合 `Tuple` 模式匹配**
适用于 **多参数匹配**：
```csharp
public string GetDirection(int x, int y) =>
    (x, y) switch
    {
        ( > 0, 0) => "Move Right",
        ( < 0, 0) => "Move Left",
        (0, > 0) => "Move Up",
        (0, < 0) => "Move Down",
        _ => "No Movement"
    };
```
✅ **可读性更强**，适用于**二维/三维输入匹配**。

---

### **总结**
| **用法**                 | **适用场景**                    | **示例**  |
|-------------------------|------------------------------|---------|
| **基本 `switch`**        | 多分支处理                    | `switch (key) { case 'W': ... }` |
| **`switch` 表达式**       | 赋值时更简洁（C# 8.0+）         | `key switch { 'W' => "Move Up", _ => "Invalid" }` |
| **多 `case` 合并**        | 处理多个 `case` 逻辑相同        | `case 'A': case 'D': break;` |
| **`switch` + `enum`**     | 处理固定状态（状态机）         | `switch (GameState.Playing) { ... }` |
| **`switch` + `when`**     | 复杂条件匹配（C# 7.0+）        | `case int n when n > 0:` |
| **`switch` + `Tuple`**    | 多条件匹配（C# 8.0+）         | `(x, y) switch { ( > 0, 0) => "Move Right" }` |

如果你的 `switch` 逻辑复杂，优先考虑 **`switch` 表达式或 `Tuple` 模式匹配**，让代码更清晰！🚀