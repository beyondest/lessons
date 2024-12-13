# QA

1. Q: Dereferencing pointer 
    ```c
        *a = (int*)malloc(sizeof(int)); // 分配内存给 *a
        **a = 10;  // 修改 *a 指向的内存
    ```
    this will raise warning C6011: Dereferencing NULL pointer '*a'.  
    A: Add if statement to check if *a is not NULL before dereferencing it.
    ```c
        *a = (int*)malloc(sizeof(int)); // 分配内存给 *a
        if(*a) {
            **a = 10;  // 修改 *a 指向的内存
        }
    ```
