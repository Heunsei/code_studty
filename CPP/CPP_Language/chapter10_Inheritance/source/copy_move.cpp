#include <iostream>

using namespace std;

class Base{
private:
    int value;
public:
    Base(): value{0} { std::cout << "Base no-args constructor" << std::endl; }
    Base(int x): value{x} { std::cout << "Base no-args constructor" << std::endl; }
    Base(const Base &other)
        : value{other.value}{
        std::cout << "Base copy constructor" << std::endl;
    }
    Base &operator=(const Base &rhs){
        std::cout << "Base operator = " << std::endl;
        if(this == &rhs)
            return *this;
        value = rhs.value;
        return *this;
    }
    ~Base() {std::cout << "Base destructor" << endl; }
};

class Derived : public Base{
private:
    int doubled_value;
public:
    Derived()
        : Base{}{
            std::cout << "Derived no-args constructor" << std::endl;
    }
    Derived(int x)
        : Base{x}, doubled_value{x*2}{
            std::cout << "int Derived constructor" << std::endl;
    }
    Derived(const Derived &other)
        : Base(other), doubled_value {other.doubled_value}{
            std::cout << "Derived copy constructor" << std::end;
    }
    Derived &operator=()
}
 