#include <iostream>
#include <cstring>
#include "Mystring.h"
// 기본생성자
Mystring::Mystring()
  :str{nullptr}{
    str = new char[1];
    *str = '\0';
}
// 오버로딩 생성자
Mystring::Mystring(const char *s)
:str{nullptr}{
    if(s==nullptr){
        str = new char[1];
        *str = '\0';
    }else{
        str = new char[std::strlen(s) + 1];
        strcpy(str, s);
    }
}
// 복사 생성자
Mystring::Mystring(const Mystring &source)
:str{nullptr}{
    str = new char[strlen(source.str) + 1];
    strcpy(str, source.str);
    std::cout <<"Copy constructor used" << std::endl;
}
// 이동 생성자
Mystring::Mystring(Mystring &&source)
:str{source.str}{
    source.str = nullptr;
    std::cout << "Move constructor used" << std::endl;
}
// 파괴자
Mystring::~Mystring(){
    delete [] str;
}
// 대입 연산자
Mystring &Mystring::operator=(const Mystring &rhs){
    std::cout << "Using copy assignment" << std::endl;
    if(this == &rhs)
        return *this;
    delete [] str;
    str = new char[strlen(rhs.str) + 1];
    strcpy(str, rhs.str);
    return *this;
}
// 이동 대입 연산자
Mystring &Mystring::operator=(Mystring &&rhs){
    std::cout << "using move assignment" << std::endl;
    if(this == &rhs)
        return *this;
    delete [] str;
    str = rhs.str;
    rhs.str = nullptr;
    return *this;
}

void Mystring::display() const { 
    std::cout << str << ":" << get_length() << std::endl;
}

int Mystring::get_length() const {return strlen(str);}
const char *Mystring::get_str() const {return str;}
// 출력 오버로딩
std::ostream &operator<<(std::ostream &os, const Mystring &rhs){
    os << rhs.str;
    return os;
}
// 입력 오버로딩
std::istream &operator>>(std::istream &in, Mystring &rhs){
    char *buff = new char[1000];
    in >> buff;
    rhs = Mystring{buff};
    delete [] buff;
    return in;
}  
