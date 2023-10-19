#include <iostream>

// interface 생성
// 이친구를 상속받는 클래스들은 print를 할 수 있도록 해준다
class I_Printalbe{
    friend std::ostream &operator<<(std::ostream &os , const I_Printalbe &obj);
public:
    virtual void print(std::ostream &os) const = 0; // pure virtual function 
};

// 프렌드 함수
std::ostream &operator<<(std::ostream &os , const I_Printalbe &obj){
    obj.print(os);
    return os;
}

class Account : public I_Printalbe{
public:
    virtual void witdraw(double amount){
        std::cout << "Account withdraw" << std::endl;
    }
    virtual void print(std::ostream &os) const override{
        os << "Account display";
    }
    // 파괴자
    virtual ~Account(){}
};

class Checking : public Account{
public:
    virtual void witdraw(double amount){
        std::cout << "Checking withdraw" << std::endl;
    }
    virtual void print(std::ostream &os) const override{
        os << "Checking display";
    }
    virtual ~Checking(){}
};

class Saving : public Account{
public:
    virtual void witdraw(double amount){
        std::cout << "Saving withdraw" << std::endl;
    }
    virtual void print(std::ostream &os) const override{
        os << "Saving display";
    }
    virtual ~Saving(){}
};

class Trust : public Account{
public:
    virtual void witdraw(double amount){
        std::cout << "Trust withdraw" << std::endl;
    }
    virtual void print(std::ostream &os) const override{
        os << "Trust display";
    }
    virtual ~Trust(){}
};

class Dog : public I_Printalbe{
public:
    virtual void print(std::ostream &os) const override{
        std::cout << "woof woof";
    }
};

void print(const I_Printalbe &obj){
    std::cout << obj << std::endl;
}

int main(){
    // Dog *dog = new Dog();
    // std::cout << *dog << std::endl; // woof woof
    // print(*dog);                    // woof woof

    Account *p1 = new Account();
    std::cout << *p1 << std::endl;      // account
    print(*p1);                         // account

    Account a;
    std::cout << a << std::endl;        // account

    Checking c;
    std::cout << c << std::endl;        // Checking

    Saving s;
    Account &p2 = s;
    print(p2);                          // Saving

    delete p1;


}