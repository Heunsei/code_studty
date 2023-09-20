#include <iostream>
#include <string>

using namespace std;

class Player{
private:
  std::string name;
  int health;
  int xp;
public:
  std::string get_name() const {return name;}
  void set_name(std::string n) {name = n;}
  
  Player();
  Player(std::string name_val);
  Player(std::string name_val, int health_val, int xp_val);
};
Player::Player()
  :Player{"None", 0, 0}{
}

Player::Player(std::string name_val, int health_val, int xp_val)
  :name{name_val}, health{health_val}, xp{xp_val} {
}

void display_player_name(const Player &p){
  cout << p.get_name() << endl;
}

int main(){
  // 속성값을 어떤것도 바꿀 수 없음
  const Player villain {"Villain", 100, 55};
  Player hero {"Hero", 100, 15};
  // villain.set_name("super villain")  error!
  // cout << villian.get_name() << endl; error!
  // cout << hero.get_name() << endl; okay!
  return 0;
}
