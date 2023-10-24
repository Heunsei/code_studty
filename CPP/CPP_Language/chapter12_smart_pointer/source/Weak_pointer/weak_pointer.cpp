#include <iostream>
#include <memory>

using namespace std;

class B;    // forward declartion 
// 아래에서 A가 B가뭔지 모르니까 미리 선언

class A{
    std::shared_ptr<B> b_ptr;
public:
    // B를 가리키는 포인터 설정
    void set_B(std::shared_ptr<B> &b){
        b_ptr = b;
    }
    A() { cout << "A Constructor" << endl;}
    ~A() { cout << "A Destructor" << endl;}
};

class B{
    std::weak_ptr<A> a_ptr;   // shared의 경우 파괴자가 호출되지 않음
public:
    // A를 가리키는 포인터 설정
    void set_A(std::shared_ptr<A> &a){
        a_ptr = a;
    }
    B() { cout << "B Constructor" << endl; }
    ~B() { cout << "B Destructor" << endl; }
};

int main(){
    // 서로가 서로를 바라보는 형태
    shared_ptr<A> a = make_shared<A>(); // a는 A클래스를 바라봄
    shared_ptr<B> b = make_shared<B>(); // b는 B클래스를 바라봄

    a -> set_B(b);  // A는 B를 바라봄
    b -> set_A(a);  // B가 A를 바라봄

    return 0;
}