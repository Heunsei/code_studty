#include <iostream>
#include <vector>

using namespace std;

class Account{
public:
    virtual void withdraw(double amount){
        std::cout << "In Account:withdraw" << std::endl;
    }
    // 가상 파괴자
    virtual ~Account(){}
};

class Checking : public Account{
    virtual void withdraw(double amount){
        std::cout << "In Checking:withdraw" << std::endl;
    }
    // 가상 파괴자
    virtual ~Checking(){}
};

class Saving : public Account{
    virtual void withdraw(double amount){
        std::cout << "In Saving:withdraw" << std::endl;
    }
    // 가상 파괴자
    virtual ~Saving(){}
};

class Trust : public Account{
    virtual void withdraw(double amount){
        std::cout << "In Trust:withdraw" << std::endl;
    }
    virtual ~Trust(){}
};

int main(){
    Account *p1 = new Account();
    Account *p2 = new Saving();
    Account *p3 = new Checking();
    Account *p4 = new Trust();

    p1 -> withdraw(1000);   // account 
    p2 -> withdraw(1000);   // saving
    p3 -> withdraw(1000);   // checkinig
    p4 -> withdraw(1000);   // withdraw
    

    Account* array[] = {p1, p2, p3, p4};
    for(auto i{0}; i<4; i++){
        array[i]->withdraw(1000);
    }

    std::vector<Account*> accounts {p1, p2, p3, p4};
    for(auto acc_ptr:accounts){
        acc_ptr -> withdraw(1000);
    }

    accounts.push_back(p4);
    accounts.push_back(p4);
    for(auto acc_ptr:accounts){
        acc_ptr->withdraw(1000);
    }

    delete p1;
    delete p2;
    delete p3;
    delete p4;

}