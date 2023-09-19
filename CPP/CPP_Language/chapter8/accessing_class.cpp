#include <iostream>
#include <string>

using namespace std;

class Player{
// 기본적으로 pirate값이라 밖에서 접근이 불가능함
public:
  // attributes
  string name;
  int health;
  int xp;
  // method
  // object의 속성값 name을 출력
  void talk(string text_to_say) {cout << name<< "says" << text_to_say << endl;}
  bool is_dead();
};

int main(){
  // Player object 생성
  Player heun;
  // object의 attribute에 접근
  heun.name = "Heun";
  heun.health = 100;
  heun.xp = 12;
  heun.talk("SSAFY"); 

  // pointer로 접근
  // enemy는 player object 를 가리키는 pointer
  // 초기에는 enemy에는 garbage값이 들어있음
  // 아래에 있는 속성값들도 모두 junk값
  Player *enemy = new Player;
  // dereference object
  // c초기화를 하면서 값을 넣어줌
  (*enemy).name = "Enemy";
  (*enemy).health = 100;
  enemy->xp = 15;
  enemy->talk("YFASS");



  return 0;
}