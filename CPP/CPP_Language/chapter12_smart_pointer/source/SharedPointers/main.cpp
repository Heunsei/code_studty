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
