
# CSharp Syntax
## new:
create a new instance of Class by calling a special method called constructor of that type


## out: 
Use as an extra output of a method, behind parameter MUST be assigned value in method and dont need to init outside.
```
void add(int a, int b, out sum){
    sum = a+b;
}
void main(){
    int a=5,b=3,sum;
    add(a,b,out sum);
}
```

## get && set || field && property
**字段（Field）**：  
- 直接存储数据，访问权限由 `public` / `private` 控制。  
- **如果是 `public`，就能直接读写**，无法单独限制 `set` 或 `get`。  
- **示例：**  
  ```csharp
  public class Example
  {
      public int number; // 任何地方都可以读写
  }

  Example ex = new Example();
  ex.number = 10;  // ✅ 可以直接修改
  Debug.Log(ex.number);  // ✅ 可以直接读取
  ```

**属性（Property）**：  
- **通过 `get;` 和 `set;` 来控制读取和写入权限**，可以独立设定 `get` / `set` 的访问级别。  
- **可以包含逻辑**，如数据验证或懒加载。  
- **示例：**  
  ```csharp
  public class Example
  {
      private int _number; // 私有字段，外部不能直接访问
      
      public int Number // 通过属性提供控制
      {
          get { return _number; } // 允许读取
          private set { _number = value; } // 只能在类内部修改
      }
  }

  Example ex = new Example();
  Debug.Log(ex.Number); // ✅ 允许读取
  ex.Number = 10; // ❌ 编译错误，set 是 private
  ```

**字段 vs. 属性 的关键区别**：  
| 特性 | 字段（Field） | 属性（Property） |
|------|-------------|----------------|
| 直接存储值 | ✅ 是 | ❌ 通过 `get` / `set` 访问 |
| 控制 `get` 和 `set` 权限 | ❌ 不行 | ✅ 可以 |
| 计算或处理逻辑 | ❌ 不能 | ✅ 可以 |
| 适用场景 | 内部数据存储 | 需要封装逻辑或访问控制 |

---
 **最佳实践**：
1. **普通数据用字段（private field）**：
   ```csharp
   private int health;
   ```
2. **外部访问用属性（public property）**：
   ```csharp
   public int Health
   {
       get { return health; }  // 允许获取
       private set { health = value; }  // 限制修改
   }
   ```
3. **避免直接公开字段**，改用属性控制读写，保证数据安全性。



# Naming Conventions

|              | C#            | C++                            | Python       |
|--------------|---------------|--------------------------------|--------------|
| Public       | `myVariable`  | `myVariable` / `my_variable`   | `my_variable`|
| Private      | `m_MyVariable`| `m_MyVariable`                 | `_my_variable`|
| Class        |               | `MyClass`                      |              |


# Scope Declaration
From most open to most closed:
- ``public``: access from anywhere
- ``protected`` internal: from anywhere in same project and derived Class in other projects
- ``internal``: from anywhere in same project (officially called same Assembly, you can bind projects into one Assembly)
- ``protected``: from derived Class in same project and derived Class in other projects 
- ``private protected``: from derived Class in same project
- ``private``: only accessable when you define it

# Change visiblity to other Assembly:
Add this line above the namespace/class/method you want to change:
``[assembly: InternalsVisibleTo("Assembly2)]``
