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
- 런타임동안 같은 function에 다른 의미를 할당가능
- 프로그램을 좀더 