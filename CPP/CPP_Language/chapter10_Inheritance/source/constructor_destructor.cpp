#include <iostream>

using namespace std;

class Base{
private:
    int value;
public:
    Base() : value{0} { cout << "base_no_args constructor" <<endl; }
    Base(int x) : value{x} {cout << "base(int) overloaded constructor" << endl;}
    ~Base(){cout << "Base destructor" << endl;}
};

class Derived : public Base{
private:
    int doubled_value;
public:
    Derived() : doubled_value{0} {cout << "Derived no_args constructor" << endl;}
    Derived(int x) : doubled_value{x} {cout << "Derived (int)overloaded constructor" << endl;}
    ~Derived(){cout << "Derived destructor" << endl;}
};

int main(){
    Base b;
    
    return 0;
}