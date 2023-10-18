# include <iostream>

class Base{
public:
    virtual void say_hello() const {
        std::cout << "Base class object" << '\n';
    }
    virtual ~Base() {}
};

class Derived : public Base{
public:
    virtual void say_hello() const override {
        std::cout << "Derived" << "\n";
    }
    virtual ~Derived() {}
};

int main(){
    Base *p1 = new Base();
    p1->say_hello();            // Base
    
    Derived *p2 = new Derived();
    p2->say_hello();            // Derived
    
    Base *p3 = new Derived();
    
    // derived의 say_hello에 const 키워드를 넣어서 해결
    // override만 넣으면 컴파일 에러 발생
    // const override쓰는게 정답 코드에 있음
    p3->say_hello();            // derived
}

