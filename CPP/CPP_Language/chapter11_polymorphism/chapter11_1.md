# 다형성 polymorphsim

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