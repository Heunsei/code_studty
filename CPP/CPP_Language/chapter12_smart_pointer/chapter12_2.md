## 4. shared_ptr
- 힙 오브젝트에 대해 소유권을 공유함
- shared_ptr<T>
    - 1. 힙에 있는 T타입의 오브젝트를 지시
    - 2. 같은 오브젝트에 대해 많은 shared_ptr 지시가능
    - 3. 할당되거나, 복사 가능, 이동도 가능
    - 4. 따로 count를 세고 count가 0이 된다면, 힙에 있던 관리 오브젝트는 자동으로 파괴
    - 5. shared_ptr 사용 시 인자로 주소값이 전달 된다면 ,해당객체를 자신이 첫번째로 소유하는 것 마냥 행동,
```cpp
A* a = new A();
std::shared_ptr<A> pa1(a);  // 종료시 > a를 삭제
// 참조개수 1 > 종료시 0으로 > a바로 삭제
std::shared_ptr<A> pa2(a);  // 종료시 이미 사라진 a를 삭제
// 참조개수 1

```
```cpp
{
    std::shared_ptr<int> p1 {new int {100}};
    std::cout << *p1 << std::endl;      // 100
    *p1 = 200;
    std::cout << *p1 << std::endl;      // 200
}
```

- use_count()
```cpp
{
    std::shared_ptr<int> p1 { new int{100} };
    std::cout << p1.use_count();     // 1

    std::shared_ptr<int> p2 { p1 };  // 같은곳을 가리킴
    std::cout << p1.use_count();     // 2

    p1.reset();     // p1 > nullptr, decrement use_count
    std::cout << p1.use_count() << std::endl;   // 0
    std::cout << p2.use_count() << std::endl;   // 1
}
```
- shared_ptr<T> 는 copy 가능
```cpp
{
    std::vector<std::shared_ptr<int>> vec;
    std::shared_ptr<int> ptr {new int{100}};
    vec.push_back(ptr);         // 복사 가능
    // unique_ptr은 vec.push_back(std::move(ptr))
    std:: cout << ptr.use_count() << std::endl;  //2
}
```

- std::make_shared 사용
```cpp
{
    std::shared_ptr<int> p1 = std::make_shared<int>(100);
    std::shared_ptr<int> p2 {p1};
    std::shared_ptr<int> p3;
    p3 = p1;
}
```