# 다형성 polymorphsim
### 참고 블로그 : https://dream-and-develop.tistory.com/103


# 1.다형성 이란?
- OOP의 기능
### 1. 다형성
    - compile-time / early binding / static binding
        - early binding
            1. 기본적으로 static 바인딩이라 불려짐
            2. method 혹은 function이 컴파일 시간에 호출됨
            3. 컴파일러가 프로그램을 실행하기 전에 확인 하는 것
            4. function overloading / operator overloading 
    - Run-time / late binding / dynamic binding
        - late binding
            1. dynamic binding이라 불림
            2. 런타임에 실행.
            3. method 혹은 function이 서언된 타입보다 오브젝트의 실질적인 타입으로 결정됨
            4. function overriding
```cpp
class Animal {
public:
    virtual void sound() {
        cout << "Some sound" << endl;
    }
};

class Dog : public Animal {
public:
    void sound() override {
        cout << "Woof" << endl;
    }
};

int main() {
    Animal* myAnimal = new Dog();
    myAnimal->sound();  // This is an example of late binding
    delete myAnimal;
    return 0;
}
```
- myAnimal은 animal을 가리키지만 late binding 때문에 dog sound가 호출됨

### 2. 런타임 다형성

- dynamic binding이 없을 때
```cpp
Account a;
a.withdraw(100);
Account *p = new Trust();  
p -> withdraw(1000);        
```
1. p는 account object를 가리키는 포인터. 따라서 p는 account object의 주소를 포함한다.
2. trust account를 힙에 동적으로 생성 그 후 그것의 주소를 p에 할당
3. p는 account를 홀딩할 수 있고 trust는 account니까
4. p가 가리키는 withdraw를 실행 > 
5. 기본적으로 static binding을 쓰니 컴파일러는 런타임 때 p가 어떤 account object의 타입을 가리키는지 모른다. 오직 p가 account만 가리킨다는 것을 암
6. 따라서 account::withdraw()를 호출함

- dynamic bindg 사용 할 때

```cpp
Account a;
a.withdraw(1000); // account::withdraw()

Saving b;
b.withdraw(1000); // Saving::withdraw()

Checking c;
c.withdraw(1000); // Checking::withdraw()

Trust d;
d.withdraw(1000); // Trust::withdraw()

Account *p = new Trust();
p -> withdraw(1000); // Trust::withdraw
```

- 컴파일 하는동안 할당하고 값을 저장하지 말고 런타임 때 바인딩을 해라.

```cpp
void display_account(const Account &acc){
    acc.display();
    // depending on the object's type at run time
}

Account a;
a.withdraw(1000); // account::withdraw()

Saving b;
b.withdraw(1000); // Saving::withdraw()

Checking c;
c.withdraw(1000); // Checking::withdraw()

Trust d;
d.withdraw(1000); // Trust::withdraw()
```
- 포인터 또는 참조를 base에 사용할 때 마다 바인딩은 컴파일 시간이 아니라 런타임때 끝남
- display_account는 제공받은 object의 타입을 기반으로 display_account를 호출할것임


## 3. base class pointer
- c++에서 컴파일러가 함수를 호출할 때, 어느 블록에 있는 함수를 호출해야하고, 해당함수가 저장된 메모리위치도 알아야함.
함수를 호출하는 코드에서 어느블록에 있는 함수를 실행하라는 의미로 해석하는것을 바인딩 이라고 함
- 가상함수의 호출은 컴파일러가 어떤 함수를 호출해야 하는지 미리 알 수 없음, 프로그램이 실행될 때 객체를 결정하므로, 컴파일시간에 해당 객체를 특정할 수 없기 때문.
- Virtual Function(가상함수)
    - 기본 클래스 내에서 선언되어 파생클래스에 의해 재정의 되는 멤버함수
    - 포인터 또는 기본 클래스에 대한 참조를 사용하여 파생 클래스의 객체를 참조하면 해당 객체에 대해 가상 함수를 호출하고 파생 클래스의 함수를 실행가능
    - 런타임동안 다형성을 구현하는데 사용

    - 규칙
        - 1. 클래스의 공개 섹션에 선언
        - 2. 가상 함수는 static일 수 없으며 frend함수가 될 수도 없다
        - 3. 실행시간 다형성을 얻기 위해 base class의 포인터 또는 참조를 통해 접근한다
        - 4. 가상함수의 반환형과 매개변수는 기본 클래스와 파생 클래스에서 동일함
        - 5. 클래스는 가상 소멸자를 가질 수 있지만 가상 생성자는 가질 수 없음


## 4. Virtual function
- 가상함수를 base class pointer 또는 reference로 호출


## 5. Virtual destructors 가상 파괴자
- 만약 클래스가 가상 함수를 가지고 있다면 '언제나' public virtual desturctor를 제공해야함
- 그렇지 않으면 기본 클래스 포인터로 파생 클래스 객체를 생성 하였을때, 생성된 파생 객체에 대해 소멸자가 실행되지 않음.
- 만약 base 클래스 파괴자가 가상이라면 derived클래스 파괴자 또한 가상이다
```c++
class Account{
public:
    virtual void withdraw(double amount);
    virtual ~Account();
};
```

```cpp
Base *p = new Derived();    // 기본 클래스 포인터로 파생클래스 객체 생성
delete p;   // 기본 클래스의 소멸자만 실행  
```

## 6. Override specifier
- 오버라이드 지정자, 재정의 키워드를 사용해 기본 클래스에서 가상 함수를 재정의하는 멤버 함수를 지정
- // void draw();
- void drow() override; // 컴파일러한테 오버라이딩 확인하도록 시킴

- const 지정자
```cpp
class Base{
public:
    virtual void say_hello() const{
        std::cout << "Hello - base class object" << std::endl;
    }
    virtual ~Base(){}
};

class Derived : public Base{
public:

    virtual void say_hello()  { // const가 없으니 overriding 되지 않음
        std::cout << "Derived class" << std::emdl;
    }
    virtual ~Derived(){}
};

Base p1 = new Base();
p1->say_hello();    // dynamic-bound. base
Base p2 = new Derived();
p2->say_hello();    // static-bound. base
```

- override specifier 
```cpp
class Base{
public:
    virtual void say_hello() const{
        std::cout << "Base" << std::endl;
    }
    virtual ~Base();
};

class Derived : public Base {
public:
    virtual void say_hello() override {     // compile error, const 안넣었어용
        std::cout << "Derived" << std::endl;
    }
    virtual ~Derived(){}
}
```

- final 특별자
    - 클래스에 사용 경우 class가 derived 되는것을 방지함
        - 그 클래스를 상속하려할때 그것을 막음
    - 메소드 레벨에 사용경우 메소드가 메소드 클래스에서 overridein 되는것을 방지함.

```cpp
class A{
public:
    virtual void do_somiething();
};

class B: public A{
    virtual void do_somiething() final; // 오버로딩 방지
};

class C: public B{
    virtual void do_something(); // compiler error
}
```