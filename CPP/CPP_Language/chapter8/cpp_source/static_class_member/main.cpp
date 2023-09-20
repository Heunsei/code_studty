#include <iostream>
#include "Player.h"

using namespace std;

void display_active_player(){
  cout << "Active Player" << Player::get_num_players() << endl;
}

int main(){
  display_active_player();
  Player Hero{"Hero"};
  display_active_player();
  return 0;
}