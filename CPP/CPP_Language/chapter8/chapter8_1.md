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
