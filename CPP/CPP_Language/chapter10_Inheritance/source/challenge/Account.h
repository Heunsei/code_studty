#ifndef _ACCOUNT_H_
#define _ACCOUNT_H_
#include <iostream>
#include <string>

constexpr int add(int a, int b) { return a + b; }
// 변수에 붙어있으면 컴파일시 계산이 되어있어야한다.
constexpr int six = add(1, 5);

class Account{
    friend std::ostream &operator<<(std::ostream &os, const Account &Account);
private:
    // constexpr > 컴파일 시간 상수를 만드는 키워드
    // 컴파일 때 계산이 가능하다? 
    static constexpr const char *def_name 
}
#endif

