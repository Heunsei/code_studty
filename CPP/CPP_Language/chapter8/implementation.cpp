#include <iostream>
#include <string>

using namespace std;

class Account{
private:
  // attributes
  string name;
  int balance;

public:
  // declared inline
  void set_balance(double bal)  {balance = bal;}
  double get_balance()  {return balance;}

  // this method will be declared outside class declaration
  void set_name(string n);
  string get_name();

  bool deposit(double amount);
  bool withdraw(double amount);
};

void Account::set_name(string n){
  name = n;
}

string Account::get_name(){
  return name;
}

bool Account::deposit(double amount){
  balance += amount;
  return true
}

bool Account::withdraw(double amount){
  if(balance - amount >= 0){
    balance -= amount;
    return true;
  }
  else{
    return false;
  }
}

int main(){
  Account heun_account;
  // 속성값은 밖에서 접근하지못하게 하고
  // get이나 set속성으로 수정할수 있게 한다
  heun_account.set_name("heun_account");
  heun_account.set_balance(1000.0);
}
