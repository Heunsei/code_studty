#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Player{
  //attributes
  string name {"Player"};
  int health {100};
  int xp {3};
  //methods
  void talk(string);
  bool is_dead();
};

class Account{
  string name {"Account"};
  double balance {0.0};
  // method
  bool deposit(double);
  bool withdraw(double);
};
int main(){
  Account heun_account;

  Player heun;
  Player hero;

  Player players[] {heun, hero};

  vector<Player> player_vec {heun};
  player_vec.push_back(hero);

  Player *enemy {nullptr};
  enemy = new Player;

  delete enemy;
  return 0;
}
