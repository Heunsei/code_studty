#ifndef _SAVING_ACCOUNT_H_
#define _SAVING_ACCOUNT_H_
#include "Account.h"

class Saving_Account : public Account{
private:
    static constexpr const char *def_name = "Unnamed Savings Account";
    static constexpr double def_balance = 0.0;
    static constexpr double def_int_rate = 0.0;
protected:
    double int_rate;
public:
    Saving_Account(std::string name = def_name, double balance = def_balance, double int_rate = def_int_rate);
    virtual bool deposit(double amount) override;       // account의 함수를 상속
    virtual bool withdraw(double amount) override;      // account의 함수를 상속
    virtual void print(std::ostream &os) const override;
    virtual ~Saving_Account() = default;
};
#endif