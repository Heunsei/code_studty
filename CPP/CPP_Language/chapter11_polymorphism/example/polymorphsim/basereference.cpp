#include <iostream>

class Account{
public:
    virtual void withdraw(double amount){
        std::cout << "in account" << std::endl;
    }
    virtual ~Account(){}
};

class Checking : public Account{
public:
    virtual void withdraw(double amount){
        std::cout << "Checking" << std::endl;
    }
    virtual ~Checking(){}
};

class Saving : public Account{
public:
    virtual void withdraw(double amount){
        std::cout << "Saving" << std::endl;
    }
    virtual ~Saving(){}
};

class Trust : public Account{
public:
    virtual void withdraw(double amount){
        std::cout << "Trust" << std::endl;
    }
    virtual ~Trust(){}
};

void do_withdraw(Account &account, double amount){
    account.withdraw(amount);
}

int main(){
    Account a;
    Account &ref = a;
    ref.withdraw(1000); // account

    Trust t;
    Account &ref1 = t;
    ref1.withdraw(1000); // Trust

    Account a1;
    Saving a2;
    Checking a3;
    Trust a4;

    do_withdraw(a1, 1000);  // account
    do_withdraw(a2, 2000);  // saving
    do_withdraw(a3, 3000);  // checking
    do_withdraw(a4, 4000);  // trust
    // do_withdraw는 인자로 Account 객체를 받지만 saving, checking
    // trust는 account로부터 상속받은 객체기 때문에 각자의
    // 이름을 출력시킨다

    return 0;
}