#include <iostream>
#include <memory>
#include <vector>
#include "Savings_Account.h"

class Test{
private:
    int data;
public:
    Test() : data{0} { std::cout << "Test constructor(" << data << ")" <<std::endl;}
    Test(int data) : data {data} {std::cout << "Test constructor (" << data << ")" << std::endl;}
};

int main(){
    std::shared_ptr<int> p1 {new int {100}};    // 1
    std::cout << "Use Count" << p1.use_count() << std::endl;

    std::shared_ptr<int> p2 {p1};            
    std::cout << "Use Count" << p1.use_count() << std::endl; // 2

    p1.reset();      // p1 > null out , p2 > int {100} 지칭
    std::cout << "Use Count" << p1.use_count() << std::endl; // 0
    std::cout << "Use Count" << p2.use_count() << std::endl; // 1
}