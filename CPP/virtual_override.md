是的，在 C++ 中，如果一个虚函数在类层次结构中被重写了，子类仍然可以继续重写该函数。

### **虚函数的继承规则**
1. **虚函数的性质是继承的**：
   - 当一个类（如 `A`）中定义了虚函数，即使该虚函数被其子类（如 `B`）重写了，该函数仍然是虚函数。
   - 因此，`C` 可以进一步重写这个虚函数。
2. **编译器会沿着类层次结构检查重写的合法性**：
   - `C` 中的重写函数必须与 `B` 中的虚函数签名匹配（包括函数名、参数类型、返回类型等）。

---

### **示例代码**

```cpp
#include <iostream>
using namespace std;

class A {
public:
    virtual void show() const {
        cout << "A::show()" << endl;
    }
};

class B : public A {
public:
    void show() const override { // 重写 A 的 show()
        cout << "B::show()" << endl;
    }
};

class C : public B {
public:
    void show() const override { // 再次重写 B 的 show()
        cout << "C::show()" << endl;
    }
};

int main() {
    A* obj1 = new A();
    A* obj2 = new B();
    A* obj3 = new C();

    obj1->show(); // 输出：A::show()
    obj2->show(); // 输出：B::show()
    obj3->show(); // 输出：C::show()

    delete obj1;
    delete obj2;
    delete obj3;

    return 0;
}
```
Output:
```
A::show()
B::show()
C::show()
```


---

### **解释**
1. **多层重写的动态绑定**：
   - 无论对象是 `A*`、`B*` 还是 `C*` 类型，调用虚函数时会根据实际的对象类型动态绑定到相应的实现。
2. **C 的 `show()` 覆盖了 B 的 `show()`**：
   - 即使 `B` 重写了 `A` 的 `show()`，`C` 仍然可以进一步重写。
3. **动态多态性**：
   - 虚函数的动态绑定确保了运行时根据对象的实际类型调用正确的函数。

---

### **注意事项**
1. **`override` 提高安全性**：
   - 在 `B` 和 `C` 中标记 `override` 可以让编译器检查是否正确覆盖了父类的虚函数，避免函数签名不匹配的错误。
2. **覆盖优先级**：
   - 如果子类未显式重写虚函数，将默认继承父类最近一层的实现。
3. **纯虚函数的影响**：
   - 如果 `A` 中的虚函数是纯虚函数（即 `= 0`），`B` 或 `C` 必须提供实现，否则 `B` 和 `C` 也会被视为抽象类，不能实例化。

**示例：**
```cpp
class A {
public:
    virtual void show() const = 0; // 纯虚函数
};

class B : public A {
public:
    void show() const override {
        cout << "B::show()" << endl;
    }
};

class C : public B {
public:
    void show() const override {
        cout << "C::show()" << endl;
    }
};
```


---

### **总结**
- 类层次结构中的虚函数可以在每一层子类中继续被重写。
- 即使子类已经重写了虚函数，孙类仍然可以进一步重写它。
- 使用 `override` 可以提高代码的安全性和可读性。