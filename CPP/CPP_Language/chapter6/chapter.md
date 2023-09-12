# Function
- C++ programs
  - C++ STL , function and classes
  - own function and classes
  - separate code into logical self - contained units
  - units can be reuse
  
## Defining Functions
- parameter list
  - the var passed into the funtcion
  - must be specified
- return type
  - type of data that returnes from thd function
- body
  - the statements that are excuted when the function is callsd
  - in curly braces {}

```cpp
int function_name(int par)
{
  statements(s);
  return 0;
}
```

# Function Prototypes
- 프로그램이 커질때 선언을먼저하고 나중에 정의하는것
```cpp
int function_name(); // prototype

int function_name()
{
  statements(s);
  return 0;
}
```