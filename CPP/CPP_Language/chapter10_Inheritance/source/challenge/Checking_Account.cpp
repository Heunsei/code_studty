#include "Checking_Account.h"

// 생성자
Checking_Account::Checking_Account(std::string name, double balance)
    // base class 생성자 호출
    : Account {name, balance} {
}

// 인출 
bool Checking_Account::withdraw(double amount) {
    amount += per_check_fee;
    return Account::withdraw(amount);
}

std::ostream &operator<<(std::ostream &os, const Checking_Account &account) {
    os << "[Checking_Account: " << account.name << ": " << account.balance  << "]";
    return os;
}

