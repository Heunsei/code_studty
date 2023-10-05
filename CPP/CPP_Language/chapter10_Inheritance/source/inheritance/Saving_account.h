#ifndef _SAVING_ACCOUNT_H_
#define _SAVING_ACCOUNT_H_
#include "Account.h"

class Saving_Account:public Account
{
public:
    double int_rate;
    
    Saving_Account();
    ~Saving_Account();
    void deposit(double amount);
    void withdraw(double amount);
};
#endif