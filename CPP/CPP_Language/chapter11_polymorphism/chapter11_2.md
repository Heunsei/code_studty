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

## 9 Abstract class as interface
- C++에서의 interface
    1. 0개 이상의 기본 인터페이스에서 상속 가능
    2. 기본 클래스에서 상속할 수 없음
    3. 공용 순수 가상 메서드만 포함할 수 있음
    4. 생성자, 소멸자, 연산자를 포함할 수 없음
    5. 정적 메서드를 포함할 수 없음
    6. 데이터 멤버를 포함할 수 없음
- 유저가 정의한 자료타입을 출력하려면 printable interface class를 만들어 해결

```cpp
class Printable{
    friend ostream &operator<<(ostream &, const Printable &obj);
public:
    virtual void print(ostream &os) const = 0;
    virtual ~Printable() {};
};

ostream &operator<<(ostream &os, const Pritable &obj){
    ogj.print(os);
    return os;
}

class Any_Class : public Printable{
public:
    //반드시 override해야함
    virtual void print(ostream &os) override{
        os << "From Any_Class";
    }
};


```