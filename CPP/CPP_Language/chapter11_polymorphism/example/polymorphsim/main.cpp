#include <iostream>

using namespace std;

class Base{
public:
    void say_hello() const{
        std::cout << "hello - i'm a Base class object" << std::endl;
    }
};

class Derived : public Base{
public:
    void say_hello() const{
        std::cout << "hello - i'm a Dreived class object" << std:endl;
    }
};

// base object를 가져오는 데 derived는 base를 상속받음
// 하지만 우리는 static 바인딩을 쓰고있기 때문에
// Derived의 문장이 출력되지 않음
void greeting(const Base &obj){
    // 여기는 항상 base로 binding 되어있음
    // Base:
    obj.say_hello();
}

int main(){
    Base b;
    b.say_hello();  // base

    Derived d;
    d.say_hello();  // derived

    greeting(b);    // base
    greeting(d);    // base

    Base *ptr = new Derived();
    ptr -> say_hello();    // base

    return 0;
}

