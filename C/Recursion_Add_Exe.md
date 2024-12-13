# A Bad Code which will Add Console Prompt Forever

```c
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>  // 提供 _kbhit() 和 _getch() 函数

// 全局变量，用于存储共享信息
int sharedData = 0;

// 互斥锁，用于同步线程访问共享数据
CRITICAL_SECTION cs;

// 线程1：读取用户输入并更新共享数据
DWORD WINAPI InputThread(LPVOID lpParam) {
    while (1) {
        // 非阻塞输入检查
        if (_kbhit()) {
            // 锁住互斥锁，防止其他线程访问共享数据
            EnterCriticalSection(&cs);

            printf("Enter a number to update shared data: ");
            sharedData = _getch() - '0';  // 读取用户输入并赋值给共享变量

            // 释放互斥锁
            LeaveCriticalSection(&cs);
        }
        Sleep(100);  // 降低CPU使用率，避免死循环占用过多CPU资源
    }
    return 0;
}

// 线程2：打印共享数据
DWORD WINAPI PrintThread(LPVOID lpParam) {
    while (1) {
        // 锁住互斥锁，确保线程安全
        EnterCriticalSection(&cs);

        printf("Shared Data: %d\n", sharedData);  // 打印共享数据

        // 释放互斥锁
        LeaveCriticalSection(&cs);

        Sleep(2000);  // 每 2 秒打印一次
    }
    return 0;
}

int main() {
    // 初始化互斥锁
    InitializeCriticalSection(&cs);

    // 创建线程来模拟进程行为
    HANDLE thread1, thread2;

    // 创建线程1
    thread1 = CreateThread(NULL, 0, InputThread, NULL, 0, NULL);
    if (thread1 == NULL) {
        printf("Failed to create InputThread\n");
        return 1;
    }

    // 创建线程2
    thread2 = CreateThread(NULL, 0, PrintThread, NULL, 0, NULL);
    if (thread2 == NULL) {
        printf("Failed to create PrintThread\n");
        return 1;
    }

    // 使用 system() 启动第二个命令行窗口并运行输出线程
    system("start cmd /K \"start /min /wait D:/WS_VS/OS_C/x64/Debug/Test.exe print_thread\"");

    // 启动当前命令行窗口以进行输入
    system("start cmd /K \"start /min /wait D:/WS_VS/OS_C/x64/Debug/Test.exe input_thread\"");

    // 等待线程结束
    WaitForSingleObject(thread1, INFINITE);
    WaitForSingleObject(thread2, INFINITE);

    // 清理互斥锁
    DeleteCriticalSection(&cs);

    return 0;
}
```