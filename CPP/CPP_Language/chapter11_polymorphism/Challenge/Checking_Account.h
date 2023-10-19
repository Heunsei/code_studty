#ifndef _CHECKING_ACCOUNT_H_
#define _CHECKING_ACCOUNT_H_
#include <iostream>
#include <string>
#include "Account.h"

class Checking_Account: public Account {
private:
    static constexpr const char *def_name = "Unnamed Checking Account";
    static constexpr double def_balance = 0.0;
    static constexpr double per_check_fee = 1.5;
public:
    Checking_Account(std::string name = def_name, double balance = def_balance);   
    // override 받아왔다는것을 명시적으로 표시 
    virtual bool withdraw(double) override;
    virtual bool deposit(double) override;
    // override받은 print함수
    virtual void print(std::ostream &os) const override;
    // 가상 파괴자
    virtual ~Checking_Account() = default; 
};

#endif // _CHECKING_ACCOUNT_H_
