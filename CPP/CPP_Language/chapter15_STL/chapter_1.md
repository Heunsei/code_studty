# STL
## 1. Macros 
### 1. #define
- #define MAX_SIZE 100
- #define NAX(a,b) ((a>b) ? a : b)

### 2. Function templates
```cpp
template <typename T>
T max(T a, T b){
    return (a>b) ? a : b;
}
```

## 2. STL
### 1. container
### 2. iterators
### 3. algorithms
- #include <algorithm>
- find
```cpp
std::vector<int> vec {1,2,3};
auto loc = std::find(vec.begin(), vec.end(), 3);
if (loc != vec.end())
    std::cout << *loc << std::endl; 
```    
- for_each
```cpp
void square(int x){
    std::cout << x * x << " ";
}
std::vector<int> vec {1, 2, 3, 4};
std::for_each(vec.begin(), vec.end(), square);  // 1, 4, 9, 16
```

### 4. array (C++11)
- #include <array>
    - fixed size
    - direct element access
    - provides access to underlying raw array
    - all iterators available and do not invalidate

```cpp
std::array<int, 5> arr1 {{1,2,3,4,5}};
std::array<std::string, 3> stooges{
    std::string("Larry"),
    "Moe",
    std::string("Curly")
};
```

```cpp
std::array<int ,5> arr {1,2,3,4,5};

std::cout << arr.size(); // 5
std::cout << arr.at(0);  // 1
std::cout << arr[1];

std::cout << arr.front(); // 1
std::cout << arr.back();  // 5

std::cout << arr.empty(); // 0 (false)
std::cout << arr.max_size() // 5
```