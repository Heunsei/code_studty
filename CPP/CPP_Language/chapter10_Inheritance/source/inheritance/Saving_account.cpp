#include <iostream>
#include "Saving_account.h"

// 생성자
Saving_Account::Saving_Account()
    :int_rate{3.0}{
}
// 파괴자
Saving_Account::~Saving_Account(){
}

void Saving_Account::deposit(double amount){
    std::cout << "Saving Account deposit called with" << amount << std::endl;
}

void Saving_Account::withdraw(double amount){
    std::cout << "Saving Account withdraw called with" << amount << std::endl; 
}