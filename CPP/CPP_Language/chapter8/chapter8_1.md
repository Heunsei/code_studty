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