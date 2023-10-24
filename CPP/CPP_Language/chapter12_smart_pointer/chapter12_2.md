## 4. shared_ptr
- 힙 오브젝트에 대해 소유권을 공유함
- shared_ptr<T>
    - 1. 힙에 있는 T타입의 오브젝트를 지시
    - 2. 같은 오브젝트에 대해 많은 shared_ptr 지시가능
    - 3. 할당되거나, 복사 가능, 이동도 가능
    - 4. 따로 count를 세고 count가 0이 된다면, 힙에 있던 관리 오브젝트는 자동으로 파괴
    - 5. shared_ptr 사용 시 인자로 주소값이 전달 된다면 ,해당객체를 자신이 첫번째로 소유하는 것 마냥 행동,

- 선언방법
- std::shared_ptr<int> p1 = std::make_shared<int>(100);

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

## 5. weak pointer
- weak_ptr<T>
    - shared_ptr로부터 생성됨
    - reference use count를 세지 않음
    - 순환 참조시 shared_ptr의 메모리가 해제되지 않는것을
    방지하기위해 사용
- 멤버 함수
    - expired() 할당받은 shared_ptr의 객체의 use_count가 0이면 true 아니면 false 리턴
    - reset() 수요한 자윈을 release
- 서로가 서로를 참조하는 shared strong ownership에서 발생하는 heap deallocation을 막기 위함

- A 는 shared_ptr<B> B는 weak_ptr<A> 이렇게 서로를 참조하면 힙에있는 저장공간이 안전하게 해제됨

## 6. custom deleters
- 함수를 활용한 삭제
```cpp
void  my_deleter(Some_Class *raw_pointer){
    delete raw_pointer;
}
std::shared_ptr<Some_Class> ptr { new SomeClass{}, my_deleter};
```
- 람다를 활용한 삭제
```cpp
shared_ptr<Test> ptr (new Test{100}, [] (Test *ptr){
    cout << "\tUsing my custom deleter" << endl;
    delete ptr;
});
```