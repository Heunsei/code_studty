#include "Account.h"


Account::Account(std::string name, double amount)
    : name{name}, balance{balance} {
}

bool Account::deposit(double amount){
    if(amount < 0 ) return false;
    else{
        balance += amount;
        return true;        
    }
}

bool Account::withdraw(double amount){
    if(balance - amount < 0) return false;
    else{
        balance -= amount;
        return true;
    }
}

void Account::print(std::ostream &os) const {
    os.precision(2);
    os << std::fixed;
    os << "[Account : " << name << " : " << balance << "]";
}