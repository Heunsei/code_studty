#include <iostream>
#include <string>

using namespace std;

class Player
{
private:
  std::string name;
  int health;
  int xp;
public:
  std::string get_name() {return name;}
  int get_health() { return health; } 
  int get_xp() { return xp; }
  Player(std::string name_val = "None", int health_val = 0, int xp_val = 0);
  // copy
  Player(const Player &source);
  // Destructor
  ~Player() {cout << "Destructor called for " << name << endl;} 
};

// 생성자 정의
Player::Player(std::string name_val, int health_val, int xp_val)
  :name{name_val}, health{health_val}, xp{xp_val}{
    cout << "Three-args constructor for " + name << endl;
}

// 복사 생성자
Player::Player(const Player &source)
: name{source.name}, health{source.health}, xp{source.xp}{
  cout << "copy constructor made copy of " << source.name << endl;
}

void display_player(Player p){
  cout << "name : " << p.get_name() << endl;
  cout << "health : " << p.get_health() << endl;
  cout << "xp : " << p.get_xp() << endl;
}


int main(){
  Player empty;
  display_player(empty);
  Player heun{"Heun",50,10};
  // 복사 생성자를 사용해 값을 전달
  display_player(heun);
  Player hero{"Hero", 100};
  Player villainP{"Villain", 100, 55};
  display_player(villainP);
  return 0;
}