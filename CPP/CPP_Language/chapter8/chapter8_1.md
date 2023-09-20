# OOP - 객체 지향 언어
## Class
- user defined data type
- has attributes
- has methods
- provides a public interface

## Object
- created from a class
- represntes a specific instance of a aclass
- each has its own identity
- each can use the defined class methods

# Declaring Class
```cpp
class Player
{
  std::string name;
  int health;
  int xp;

  void talk(std::string text_to_say);
  bool is_dead();
};

Player frank;
Player hero;

Player *enemy = new Player()
delete enemy
```

# Accessing Class member
- 멤버접근 연산자 . 를 사용
- 멤버연산자(.)는 클래스 멤버를 직접적으로 접근
- 멤버 포인터 연산자(->)는 포인터를 통해 멤버를 간접적으로 접근한다

# access modifiers
- public
  - 어디서든 접근 가능
- private
  - 클래스의 멤버나 friends 로서만 접근가능
- protected
  - 상속관계에서 사용가능 
```cpp
class Player{
// 밖에서 접근을 막아야할 속성값들을 보호
// class의 밖에서는 접근이 불가능
// 밖에서 멤버연산자로 접근하면 컴파일 에러가남
private:
  std :: string name;
  int health;
  int xp;
// 접근을 할수 있는 애들은 public으로
public :
  void talk(std::string text_to_say);
};
``` 

# implementing member method
- 1. member method have access to member attributes
  - we don't need to pass them as arguments
- 2. Can be implemented inside the class declaration
  - Implicitly inline
- 3. Can be implemented outside the class declartion
  - Class_name::method_name
- 4. Can separate specification from implementation
  - .h file for the class declaration
  - .cpp file for the class implementation
  - #include 'stad,' or <stad.h>

### constructors - 생성자
- 클래스와 같은 이름을 가지는 내부 method
- 기본적으로 만들어두지 않으면 컴파일러가 자동으로 생성해줌
- 생성자를 만들때 인자를 넣어주는걸 오버로딩 함으로써 속성값들이 비어있는 상태로 있지 않도록 해줌
```cpp
Player::Player()
  : name{"None"}, health{0}, xp{0}{
}
Player::Player(std::string name_val)
  : name{name_val}, health{0}, xp{0}{
}
Player::Player(std::string name_val, int health_val, int xp_val)
  : name{name_val}, healrh{health_val}, xp{xp_val}{
}

```
### Delegating Constructors
```cpp
Player::Player(std::string name_val, int health_val, int xp_val)
  : name{name_val}, health{health_val}, xp{xp_val}{
}
Player::Player()
  : Player{"None", 0, 0}{
}
Player::Player(std::string name_val)
  :Player{"name_val", 0, 0}{
}
```
### Default Constructor Parameters
- 디폴트로 값을 설정, 코드가 짧고 간단해짐
```cpp
class Player
{
private:
  std::string name;
  int health;
  int xp;
public:
  Player(std::string name_vla = "None",
        int health_val = 0,
        int xp_val = 0);
};
```
### Copy Constructor
- 클래스가 원시포인터(raw pointer)를 가지고 있을 경우 복사 생성자를 제공할 필요 가 있음
- 복사 생성자를 상수 참조(const reference)해서 제공하는게 필요
- 가능하다면 원시포인터 멤버를 쓰지말라 함 왜인진 몰룸
- 포인터는 복사되지 않음
```cpp
Player::Player(const Player &source)
  : name{source.name},
    health {source.health},
    xp {source.xp}{
}
```
```cpp
Account::Account(const Account &source)
  : name{source.name},
    balance{source.balance}{
}
```

## 깊은복사 & 얕은복사
- 얕은복사를 사용할 때 같은 메모리주소에 접근하고 그것이 값을 바꿔서 에러나 나오는 상황을 막아야 한다
- 새로운 메모리 주소를 할당하고 그곳에 값을 대입하는 방식으로 얕은복사에서 발생하는 문제점들을 해결한다
```cpp
Deep::Deep(const Deep &source)
{
  data = new int;
  *data = *source.data;
  cout << "Copy constructor - deep " << endl;
}
```

## 이동생성자 &&
- 복사가 여러번 일어나는 일을 막아줌
- 다른 개체 멤버 변수들의 소유권을 가져옴
- 복사 생성자와 달리 메모리 재할당을 하지 않음
- 복사 생성자보다 빠름
- 얕은 복사
```cpp
int x {100};
void func(int &num); 
func(x);  // L-value 를 불러옴
func(200) // 200은 r-value라 컴파일 에러 
// r-value 참조
void func2(int &&num);
func2(x);   // error
func2(200); // okay
```
- 오버로딩을 통해서 두가지 경우를 컨트롤 할 수 있도록 하는것이 좋아보임

- 벡터의 경우 프로그램의 뒤에서 벡터의 크기를 늘리기위해서 메모리를 확장하는데 그때마다 계속 복사를 해야하기 때문에 불필요한 연산이 너무 많이 일어남
- 얕은 복사를 하되, 소멸자를 한번만 호출할 수 있게끔 하는것
- 이동 시맨틱 이론 참고