确实，如果在 **DLL** 中没有任何导出的符号，Visual Studio 在编译时将不会生成 `.lib` 文件。这是因为 `.lib` 文件（作为导入库）包含了 DLL 中符号的引用，它告诉链接器如何找到 DLL 中的导出函数。如果 DLL 没有任何导出符号，链接器就无法创建对应的导入库文件 `.lib`，因此你无法在其他程序中链接到该 DLL。

### **为什么没有导出符号时不生成 `.lib` 文件：**

1. **导出符号与导入库：**
   - 导入库（`.lib` 文件）包含符号表和一些链接信息，告诉程序如何调用 DLL 中的函数。
   - 如果你的 DLL 没有导出任何符号（即没有 `__declspec(dllexport)` 标记的函数或类），那么 `.lib` 文件将不包含任何信息。因此，`.lib` 文件不会被生成，因为它没有用处。

2. **生成 `.lib` 文件的条件：**
   - 只有当 DLL 中有导出符号时，Visual Studio 才会生成导入库 `.lib` 文件，用来在编译时链接到 DLL 中的函数。
   - 如果 DLL 中没有任何导出函数，那么即使你设置了 `__declspec(dllexport)`，在没有符号导出的情况下，`.lib` 文件也不会生成。

### **如何测试动态库中的 `copy` 函数：**

如果你想测试你自己实现的 `copy` 函数（假设你将其放在 DLL 中），你需要确保该函数是 **导出** 的，并且有一个 `.lib` 文件来进行链接。下面是如何设置和测试这个函数的步骤。

#### 1. **实现 `copy` 函数并导出**

在你的 DLL 源代码中，确保你的 `copy` 函数被正确地导出。假设你有一个 `copy` 函数，它将一个字符串从源位置复制到目标位置。

```c
// copy.h
#ifdef COPY_EXPORTS
#define COPY_API __declspec(dllexport)  // 如果是导出 DLL 的符号
#else
#define COPY_API __declspec(dllimport)  // 如果是使用 DLL 的符号
#endif

COPY_API void copy(const char* source, char* destination);
```

```c
// copy.c
#include "copy.h"
#include <string.h>

void copy(const char* source, char* destination)
{
    strcpy(destination, source);
}
```

在上面的代码中，`__declspec(dllexport)` 用于导出 `copy` 函数，使其可以在 DLL 中被外部程序调用。

#### 2. **生成 `.lib` 文件**

确保项目中有正确的设置以导出符号：

- 在 Visual Studio 中，将项目设置为生成 **DLL**。
- 确保你在 **项目属性** -> **Configuration Properties** -> **Linker** -> **General** 中设置了 **Import Library**，指向要生成的 `.lib` 文件（例如 `copy.lib`）。
- 确保你在代码中使用了 `__declspec(dllexport)` 来导出 `copy` 函数。

在构建时，Visual Studio 会生成 `copy.dll` 和 `copy.lib`，其中 `.lib` 文件是导入库，它会在其他程序中使用。

#### 3. **编写测试代码**

假设你的测试项目已经正确设置了引用这个 DLL。你可以在测试项目中链接到 `.lib` 文件，并测试 `copy` 函数。

```cpp
// test.cpp
#include "pch.h"
extern "C" {
#include "copy.h"
}

TEST(CopyTest, CopyFunctionTest)
{
    const char* source = "Hello, World!";
    char destination[50];
    
    copy(source, destination);
    
    ASSERT_STREQ(destination, source);  // 验证目标字符串和源字符串相同
}
```

在上面的测试中：
- `copy` 函数是从 DLL 中导出的，你在测试中通过包含 `copy.h` 来使用该函数。
- 测试验证 `copy` 函数是否正确地将字符串从 `source` 复制到 `destination`。
  
#### 4. **确保测试项目的配置**

- 在测试项目中，确保你将 `copy.lib` 添加到 **Additional Dependencies** 中。
- 确保 `copy.dll` 在运行时能够被找到：
  - 将 `copy.dll` 放在测试可执行文件（`.exe`）的同一目录下。
  - 或者将 `copy.dll` 所在目录添加到 `PATH` 环境变量中。

### **总结：**

- **DLL 和 `.lib` 文件：** `.lib` 文件是 DLL 的导入库，只有当 DLL 导出符号时，`.lib` 文件才会被生成。你必须确保 DLL 中有导出函数，并且正确地使用 `__declspec(dllexport)` 来导出这些函数。
- **测试 `copy` 函数：** 你可以通过将 `copy` 函数添加到 DLL 中，生成 `.lib` 文件，然后在测试中链接 `.lib` 文件并调用函数。确保在运行时能够找到 DLL 文件。

通过这些步骤，你应该能够正确地测试 DLL 中的函数，包括像 `copy` 这样的自定义函数。