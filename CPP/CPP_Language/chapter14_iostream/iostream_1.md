# IOSTREAM
- common header files
    - 1. iostream
    - 2. fstream
    - 3. iomainip : input output manipulation
        - 입출력을 관리해주는 헤더
- commonly used stream classes
    - 1. ios
    - 2. ifstream
    - 3. ofstream
    - 4. fstream
    - 5. stringstream
- global streamobject
    - 1. cin
    - 2. cout
    - 3. cerr
    - 4. clog

## 1. stream manipulators
- 1. Boolean
    - boolaplha, noboolpalha
- 2. Intefer
    - dec, hex, oct, showbase, noshowbase, showpos, noshowpos, uppercase, nouppercase
- 3. Floating point
    - fixed, scientific, setprecision, showpoint, noshowpoint, showpos, noshowpos
- 4. Field width, justification and fill
    - setw, left, right, internal, setfill
- 5. other
    - endl, flush, skipws, noskipws, ws

### 1. Boolean
- boolean을 true or false로 출력해줌(default는 1, 0)
```cpp
//default
std::cout << (10==10) << std::endl; // 1
std::cout << std::boolalpha;
std::cout << (10==10) << std::endl; // true
std::cout << std::noboolalpha
```
- method version : std::cout.setf(std::ios::boolaplha);
- Reset to default : std::cout << std::resetiosflags(std::ios::boolalpha);  >  0또는 1로 다시 변경

### 2. Integers
- dec(10진수)
```cpp
int num {255};
// showbase를 설정해주지 않으면 ff이렇게 나와서 알아보기힘듬  
std::cout << std::showbase ; // std::noshowbase
std::cout << std::dec << num << std::endl; // 255
std::cout << std::hex << num << std::endl; // 0xff
std::cout << std::oct << num << std::endl; // 0377
```
- std::cout << std:: showpos; // std::noshowpos
    - > 양수값에 +를 붙여서 출력해줌 

- set using setf
    - std::cout.setf(std::ios::showbase);
    - std::cout.setf(std::ios::uppercase);
    - std::cout.setf(std::ios::showpos);
- reset to defaults
    - std::cout << std::resetiosflags(std::ios::basefield);
        - 10진수로 돌려놓기
    - std::cout << std::resetiosflags(std::ios::showbase);
    - std::cout << std::resetiosflags(std::ios::showpos);
    - std::cout << std::resetiosflags(std::ios::uppercase);

### 3. floating point
- DEFAULT
    - setprecision - number of digits displayed (6)
    - fixed - not fixed to specific number
    - noshowpoint - trailing zeroes are not displayed
    - nouppercase - when displaying in scientific notation
    - noshowpos - no '+' display
```cpp
double num {1234.5678};
std::cout << num << std::endl; // 1234.57 기본적으로 6자리까지 출력
```

```cpp
double num {123456789.987654321};
std::cout << std::setprecision(9);
std::cout << num << std::endl; // 123456790
```

```cpp
double num {123456789.987654321};
std::cout << std::fixed;
std::cout << num << std::endl; // 123456789.987654 
```

```cpp
double num {123456789.987654321};
std::cout << std::setprecision(3) << std::fixed;
std::cout << num << std::endl; // 123456789.988
```

```cpp
double num {12.34};
std::cout << num << std::endl // 12.34
std::cout << std::showpoint;
std::cout << num << std::endl; // 12.3400
```

- 원래대로 돌리기
    - std::cout.unsetf(std::ios::scientific | std::ios::fixed);
    - std::cout << std::resetiosflags(std::ios::floatfield);

### 4. align and fill
- skip