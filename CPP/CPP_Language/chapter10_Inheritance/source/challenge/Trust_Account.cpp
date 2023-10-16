#include "Trust_Account.h"

// 생성자 정의
Trust_Account::Trust_Account(std::string name, double balance, double int_rate)
    // base class 생성자 호출
    : Savings_Account {name, balance, int_rate}, num_withdrawals {0}  {
        
}

// base에 있는 deposit 호출
bool Trust_Account::deposit(double amount) {
    if (amount >= bonus_threshold)
        amount += bonus_amount;
    return Savings_Account::deposit(amount);
}


bool Trust_Account::withdraw(double amount) {
    // 인출 횟수가, 최대 인출 횟수보다 크거나, 최대 출금 금액을 넘어선다면 false
    if (num_withdrawals >= max_withdrawals || (amount > balance * max_withdraw_percent))
        return false;
    else {
        // 인출 횟수를 줄이기
        ++num_withdrawals;
        // 
        return Savings_Account::withdraw(amount);
    }
}

std::ostream &operator<<(std::ostream &os, const Trust_Account &account) {
    os << "[Trust Account: " << account.name << ": " << account.balance << ", " << account.int_rate 
        << "%, withdrawals: " << account.num_withdrawals <<  "]";
    return os;
}
