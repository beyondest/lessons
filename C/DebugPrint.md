# Use OutputDebugStringA to output info to output window in Visual Studio in ASCII format

```c


#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>  // Provides _kbhit() and _getch() functions

#define DebugPrintf(fmt, ...) { \
    char buffer[256]; \
    sprintf_s(buffer, sizeof(buffer), fmt, __VA_ARGS__); \
    OutputDebugStringA(buffer); \
}


// Global variable, used to store shared information
int sharedData = 0;
char buffer[50];
// Mutex, used to synchronize access to shared data by threads
CRITICAL_SECTION cs;

// Thread 1: Read user input and update shared data
DWORD WINAPI InputThread(LPVOID lpParam) {
    while (1) {
        // Non-blocking input check
        if (_kbhit()) {
            // Lock the mutex to prevent other threads from accessing shared data
            EnterCriticalSection(&cs);

            printf("Enter a number to update shared data: ");
            sharedData = _getch() - '0';  // Read user input and assign it to the shared variable

            // Release the mutex
            LeaveCriticalSection(&cs);
        }
        Sleep(100);  // Reduce CPU usage, avoid dead loop occupying too much CPU resource
    }
    return 0;
}

// Thread 2: Print shared data
DWORD WINAPI PrintThread(LPVOID lpParam) {
    while (1) {
        // Lock the mutex to ensure thread safety
        EnterCriticalSection(&cs);
        DebugPrintf("Shared data: %d\n", sharedData);
        // Release the mutex
        LeaveCriticalSection(&cs);

        Sleep(2000);  // Print every 2 seconds
    }
    return 0;
}

int main() {
    // Initialize the mutex
    InitializeCriticalSection(&cs);

    // Create threads to simulate process behavior
    HANDLE thread1, thread2;

    thread1 = CreateThread(NULL, 0, InputThread, NULL, 0, NULL);
    thread2 = CreateThread(NULL, 0, PrintThread, NULL, 0, NULL);

    if (thread1 == NULL || thread2 == NULL) {
        OutputDebugStringA("Failed to create threads\n");
        return 1;
    }

    // Wait for threads to finish
    WaitForSingleObject(thread1, INFINITE);
    WaitForSingleObject(thread2, INFINITE);

    // Clean up the mutex
    DeleteCriticalSection(&cs);

    return 0;
}
```