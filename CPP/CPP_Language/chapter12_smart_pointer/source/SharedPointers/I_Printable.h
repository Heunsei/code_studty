#ifndef _I_PRINTABLE_H_
#define _I_PRINTABLE_H_
#include <iostream>

class I_Printable
{
    friend std::ostream &operator<<(std::ostream &os, const I_Printable &obj);
public:
    virtual void print(std::ostream &os) const = 0; // 순수 가상 함수로 설정
    virtual ~I_Printable() = default;   // 가상함수 소멸자 설정
};

#endif