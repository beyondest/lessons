
# CSharp Syntax
## new:
create a new instance of Class by calling a special method called constructor of that type

## Scope Declaration
From most open to most closed:
- ``public``: access from anywhere
- ``protected`` internal: from anywhere in same project and derived Class in other projects
- ``internal``: from anywhere in same project (officially called same Assembly, you can bind projects into one Assembly)
- ``protected``: from derived Class in same project and derived Class in other projects 
- ``private protected``: from derived Class in same project
- ``private``: only accessable when you define it

## Change visiblity to other Assembly:
Add this line above the namespace/class/method you want to change:
``[assembly: InternalsVisibleTo("Assembly2)]``

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