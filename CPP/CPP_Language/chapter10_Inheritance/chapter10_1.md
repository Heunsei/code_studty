https://www.adservio.fr/post/composition-vs-inheritance
# Inheritance 상속
- 현존하는 클래스에대한 재사용을 허락하는것
- 새 클래스는 존재하던 클래스를 기반으로 하지만 개별적으로 수정해 유니크하게 만들 수 있다
- 공통의 속성을 모아 여러번 일 하는것을 막아줌

## 1. 용어와 문법
### 1. Terminology
- Base Class : 부모 클래스
- Derived Class : 자식 클래스
- Is-A relationship
    - 기초클래스의 기능의 전부를 파생 클래스도 수행할 수 있는 상태
    - public 상속
- Generalization : 일반화 
    - 비슷한 클래스들을 하나의 클래스로 합치는 것
- Specialization : 특수화

### 2. Notation
```cpp
class Account{
  // balance, deposit, withdraw  
};

class Saving_Account : public Accunt{

};
```

## 2. Inheritance and composition
- 둘 다 현존하는 클래스를 재사용 하는것
- 1. Inheritance 에서 오브젝트와 클래스는 tightly하게 묶여있다
    - 수정이 권장되지 않는다는 뜻, 부모클래스, super클래스의 변화가 자식클래스에 대해 리스크있는 변화를 야기할수있음
    
- 2. Composition 에서 오브젝트와 클래스가 loosely하게 이어져있음
    - 코드가 망가질 걱정없이 컴포넌트들을 바꿀 수 있음
    - 좀더 유연한 사용이 가능
### 상속의 장점
- Facilitates easy reusability of code from parent class without having to copy it
- Provides a clear, hierarchical structure so you can break a model into simple, accessible components.

## 3. Deriving(파생) classes from existing class
- types of inheritance in c++
    - public
        - Establishes 'is-a' relationship between derived and base classes
    - private and protected
        - Establishes 'derived class has a base class' relationship
        - different from composition

## 4. Access with public inheritance
- c는 모두 접근이 불가능하고 어떤 상속을 하는지에 따라 derived 클래스의 멤버 access가 달라짐 
- public inheritance
    - Base Class : pulbic:  a, protected :  b, private : c,
    - access in Derived Class : public : a, protected : b, c > no access 
- protected inheritance (is-a 관계가 아님)
    - Base Class : pulbic a, protected b, private c,
    - access in Derived Class : protected a, protected b, c > no access 
- private inheritance (is-a 관계가 아님)
    - Base Class : pulbic a, protected b, private c,
    - access in Derived Class : private a, private b, c > no access 
    
## 5. constructor and destructors
- 상속 클래스는 부모 클래스의 생성자, 파괴자, 오버로딩된 대입연산자, 프렌드함수들을 상속받지 않음
- 상속 클래스의 생성자, 파괴자, 대입연산자들은 base클래스 버전을 부를 수 있음
- 파생 클래스에서 기반클래스의 생성자를 명시적으로 호출해야함.

## 상속에서의 복사 이동 생성자 오버로딩.
- 기본적으로 base class에서 상속되지 않음
- 컴파일러버전이 더 나을수도 있긴하다...
- 명시적으로 dedrived class 에서 base클래스의 생성자를 호출가능
```cpp
// 명시적으로 base클래스의 생성자를 호출가능
// 파생클래스에서 생성자 옆에 기본적으로 baseclass 생성자를 호출
Derived::Derived(const Derived &other)
    : Base(other), {Derived initialization list}
{
    //code
}
```
- 복사 생성자
```cpp
class Base{
    int value;
public:
    //
    Base(const Base &other) : value{other.value}{
        cout << "Base copy constructor" << endl; 
    }
};

class Derived : public Base{
    int doubled_value;
public:
    Derived(const Derived &other)
    : Base(other), doubled_value {other.doubled_valud}{
        cout << "Derived copy constructor" << endl;
    }
};
```

- 대입연산자
```cpp
class Base{
    int value;
public:
    Base &operator=(const Base &rhs){
        if(this != &rhs){
            value = rhs.value;
        }
        return *this;
    }
};

class Derived : public Base{
    int doubled_value:
public:
    Derived &operator=(const Derived &rhs){
        if(this != &rhs){
            Base::operator=(rhs);
            doubled_value = rhs.doubled_value;
        }
        return *this;
    }
};
```

- 복사/배정의 경우 Derived클래스에 선언을 해주지 않으면 컴파일러는 자동으로 연산자를 생성해주고, base클래스의 버전을 호출함
- 만약 Derived 클래스에 복사배정자를 선언해 주었을경우 반드시 명시적으로 base버전을 불러놓아야함
- raw pointers 쓸 때 조심하자, deep copy semantics를 제공해주도록 하자

## 6. redefine base class method
- derived클래스는 base클래스의 method들을 직접적으로 불러올 수 있음.
- 또한 base클래스의 method들을 overried하거나 재정의 할수있음
- example
```cpp
class Account{
public:
    void deposit(double amount) { balance == amount; }
};

class Saving_Account : public Account{
public:
    void deposit(double amount){ // method 재정의
        amount += some_interest;
        Accout::deposit(amount) // base class의 method호출
    }
}
```
### 바인딩
- 프로그램 소스에 쓰인 각종 내부 요소, 이름 식별자들에 대해 값 또는 속성을 확정한 과정
- 정적 바인딩 : 컴파일 시점에서 이루어지는 바인딩
    - 장점 1. 컴파일시 타입에 대한 정보가 결정되어 빠르다
    - 장점 2. 타입 에러로 인한 문제를 조기에 발견할 수 있어서 안정적이다
    - 단점 : 컴파일시 결정되고 그 이후 변경이 불가능함
- 동적 바인딩 : 바인딩 과정이 실행 도중에 이루어지는 바인딩
    - A 클래스에서 생성한 print함수 A를 상속받은 B에서 오버로딩한 print함수가 존재
    ```cpp
    A* a = new A();
    a -> print();       // A클래스의 print()
    B* b = new B();
    a = b;
    a -> print()        // B클래스의 print()로 변경
    ```
    - 포인터가 가리키는 객체에 따라 호출되는 함수가 변경되는것
    - 장점 : 실행도중 필요한 객체의 함수를 호출함으로써 유연함
    - 단점 : 변수의 예상치 못한 타입으로 인한 불안정성


- c++은 기본적으로 method를 호출할 때 static binding을 사용
    - Derived클래스의 오브젝트는 Derived::deposit을 사용할거지만 우리는 Derived::deposit에서  명시적으로 Base::deposit을 사용가능