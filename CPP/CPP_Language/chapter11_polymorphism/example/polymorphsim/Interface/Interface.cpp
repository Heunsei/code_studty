#include <iostream>

class Account{
    friend std::ostream &operator<<(std::ostream &os, const Account &acc);
public:
    virtual void withdraw(double amount){
        std::cout << "Account::withdraw" << std::endl;
    }
    virtual ~Account(){}
};

std::ostream &operator<<(std::ostream &os, const Account &acc){
    os << "Account display";
    return os;
}

class Checking : public Account{
    friend std::ostream &operator<<(std::ostream &os, const Checking &acc);
public:
    virtual void withdraw(double amount) {
        std::cout << "Checking:withdraw" << std::endl;
    }
    virtual ~Checking() {}
};

std::ostream &operator<<(std::ostream &os, const Checking &acc){
    os << "Checking display";
    return os;
}

class Saving : public Account{
    friend std::ostream &operator<<(std::ostream &os, const Saving &acc);
public:
    virtual void withdraw(double amount) override{
        std::cout << "Saving:withdraw" << std::endl;
    }
    virtual ~Saving(){}
};

std::ostream &operator<<(std::ostream &os, const Saving &acc){
    os << "Saving display";
    return os;
}

int main(){
    Account *p1 = new Account();
    std::cout << *p1 << std::endl;  //account 출력

    Account *p2 = new Checking();
    std::cout << *p2 << std::endl;  // account 출력
    // 이 문제를 해결하기위해 다른 파일로 이동
    delete p1;
    delete p2;
    return 0;
}