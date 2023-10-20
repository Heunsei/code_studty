# 스마트 포인터
## 1. issues wit raw pointer
- some potentially serious problem
    1. Uninitailized pointer
    2. Memory leak
    3. dangling pointers
        - 포인터가 이미 해제된 영역을 가리키고 있는상황
    4. Not exception safe

## 2.smart pointer and RAII
- RAII(Ressource Acquisition is Initialization)
    - 스택에 할당된 메모리는 자동으로 해제되는 것을 이용한 디자인 패턴
    - 접근 가능 시점에서 이미 리소스가 초기화되었음을 보장
    - 초기화가 실패하면 throw되어 스코프 밖으로 넘어감으로 자동으로 파괴자가 호출
- 포인터의 경우 객체가 아니므로 소멸자가 호출되지 않는다. 그러니 일반적인 포인터가 아닌 포인터 객체로 만들어서 소멸될 때 자신이 가리키고 있는 객체가 delete되도록 만들자 > 스마트 포인터
- #include <momory> 에 템플릿이 저장되어있음
- Dereference (*)
- Member selection(->)
- Pointer arithmetic not supported(++, --)
```cpp
#include <memory>
{
    std::smart_pointer<some_class> ptr = 
    ptr -> method();
    cout << (*ptr) << endl;
}
// ptr will be destroyed automatically
```