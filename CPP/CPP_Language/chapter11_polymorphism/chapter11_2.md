## 7. Using Base class references
```c++
Account a;
Account &ref = a;
ref.withdraw(1000);     // Account::withdraw

Trust t;
Account &ref1 = t;
ref1.withdraw(1000);    // Trust::withdraw
```

```c++
void do_withdraw(Account &account, double amount){
    account.withdraw(amount);
}

Account a;
do_withdraw(a, 1000);   // Account::withdraw

Trust t;
do_withdraw(t, 1000);   // Trust::withdraw
```

## 8. pure virtual functions and abstract class
- Abstract class
    - 하나 이상의 순수 가상 함수를 포함하는 클래스
    - 다형성을 가진 함수의 집합을 정의 할 수 있다.
    - 동작이 정의되지 않은 순수 가상 함수를 포함하고 있으므로, 인스턴스를 생성할 수 없음
    - 상속을 통해 파생 클래스를 만들고, 파생 클래스에서 순수 가상 함수를 모두 오버라이딩 하고나서 파생클래스의 인스턴스를 생성.
- 순수 가상함수 선언방법
```cpp
virtual void member_function() = 0;
```
- Concrete class
    - 추상 클래스가 아닌 모든 클래스를 concrete라 할수있음
    - 인스턴스를 생성가능

```cpp
class Shape{
private:
    // attributes common to all shapes
public:
    virtual void draw() = 0;    // pure virtual function
    virtual void rotate() = 0;  // pure virtual function
    virtual ~Shape();
}

class Circle : public Shape{    // Concrete
// circle 인스턴스를 생성가능
private:
    // attributes common to all shapes
public:
    virtual void draw() override{

    }
    virtual void rotate() override{

    }
    virtual ~Circle();

Shape shape;                // error
Shape *ptr = new Shape();   // error

Shape *ptr = new Circle();
ptr->draw();
ptr->rotate();
// 추상화 클래스는 단독으로 인스턴스를 생성하지 못하고
// 재정의 후 포인터나 참조를 통해서 오브젝트를 생성함

};
```