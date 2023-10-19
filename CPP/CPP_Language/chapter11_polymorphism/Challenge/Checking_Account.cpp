#include "Checking_Account.h"

Checking_Account::Checking_Account(std::string name, double balance)
    : Account {name, balance} {
}

bool Checking_Account::deposit(double amount){
    // 부모 클래스의 함수 호출
    return Account::deposit(amount);
}

bool Checking_Account::withdraw(double amount) {
    amount += per_check_fee;
    return Account::withdraw(amount);
}

void Checking_Account::print(std::ostream &os) const {
    // 가장 큰수부터 2자리를 출력하겠다
    os.precision(2);
    os<< std::fixed;
    os << "[Checking_Account: " << name << ": " << balance  << "]";
}


