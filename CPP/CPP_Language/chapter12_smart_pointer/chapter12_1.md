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
- #include <memory> 에 템플릿이 저장되어있음
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

## 3. Unique Pointer
- unique_ptr<T>
    - 1. 힙에 있는 T타입의 오브젝트를 지시
    - 2. 힙에 있는 오브젝트를 지시하는 포인터는 단 하나만 존재 가능
    - 3. 할당되거나 복사 불가능, 이동은 가능
    - 4. 포인터가 파괴되었을 때, 가리키던 오브젝트도 자동으로 파괴
```cpp
{
    std::unique_ptr<int> pq {new int {100}};
    std::cout << *p1 << std::endl;  // 100
    *p1 = 200;
    std::cout << *p1 << std::endl;  // 200   
}
```

```cpp
{
    std::unique_ptr<int> p1 {new int{100}};
    std::cout << p1.get() << std::endl; // 0x564388
    p1.reset(); // p1 is now nullptr
    if(p1){
        std::cout << *p1 << std::endl;  // 실행되지않음
    }
}
```

- 유저가 정의한 class에 대해서도 사용가능
```cpp
{
    std::unique_ptr<Account> p1 {new Account {"Larry"}};
    std::cout << *p1 << std::endl; // display account

    p1->deposit(1000);
    p1->withdraw(500);
}
 ```

 ```cpp
 {
    std::vector<std::unique_ptr<int>> vec;
    std::unique_ptr<int> ptr {new int {100}};
    vec.push_back(ptr); // Error. copy not allowed
    vec.push_back(std::move(ptr));
 }
 ```
- C++14
    - new 또는 delete를 호출하지 않아도 괜찮음
 ```cpp
 {
    std::unique_ptr<int> p1 = make_unique<int>(100);
    std::unique_ptr<Account> p2 = make_unique<Account>("Curly", 4000);
    auto p3 = make_unique<Player>("Hero", 100, 100);
    std::unique_ptr<Test> t3;
    t3 = std::move(t1); // 할당이 아니라 이동이기 때문에 정상 작동, t1은 null로 변경.
 }
 ```

 ```cpp
 std::vector<std::unique_ptr<Account>> accounts;
 accounts.push_back(make_unique<Account>{"James", 10000})
 accounts.push_back(make_unique<Savings_Account>{"Billy", 4000, 5.2})
 accounts.push_back(make_unique<Trust_Account>{"James", 10000, 4.5})
 for(const auto &acc:accounts) // 에러 발생 > copy라 그럼
    std::cout << acc  << endl; // accdp const와 침조연산자 부여
    
 ```