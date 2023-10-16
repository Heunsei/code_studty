#ifndef _CHECKING_ACCOUNT_H_
#define _CHECKING_ACCOUNT_H_
#include <iostream>
#include <string>
#include "Account.h"

class Checking_Account: public Account {
    friend std::ostream &operator<<(std::ostream &os, const Checking_Account &account);
private:
    // 컴파일 시간 상수
    static constexpr const char *def_name = "Unnamed Checking Account";
    static constexpr double def_balance = 0.0;
    static constexpr double per_check_fee = 1.5;
public:
    // 생성자에게 값을 넘겨주는 과정 
    Checking_Account(std::string name = def_name, double balance = def_balance);    
    bool withdraw(double);
    // Inherits the Account::deposit method
};

#endif // _CHECKING_ACCOUNT_H_
