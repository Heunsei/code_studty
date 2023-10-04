#include <iostream>
#include <cstring>
#include "mystring.h"

// constructor
Mystring::Mystring()
    : str{nullptr}{
        str = new char[1];
        *str = '\0';
}

// overloaded constructor
Mystring::Mystring(const char *s)
    :str{nullptr}{
        if(s==nullptr){
            str = new char[1];
            *str = '\0';
        }else{
            str = new char[strlen(s)+1];
            strcpy(str, s);
        }
}

// copy constructor
Mystring::Mystring(const Mystring &source)
    :str{nullptr}{
        str = new char[strlen(source.str)+1];
        strcpy(str, source.str);
    }


// move constructor
// Mystring 객체를 복사
Mystring::Mystring(Mystring &&source)
    :str(source.str){
        source.str = nullptr;
}


Mystring::~Mystring(){
    delete [] str;
}

// 깊은복사 사용.
Mystring &Mystring::operator=(const Mystring &rhs){
    if(this == &rhs)
        return *this;
    delete [] str;
    str = new char[strnlen(rhs.str)+1]
    strcpy(str, rhs.str);
    return *this
}

// 얕은복사.
Mystring &Mystring::operator=(Mystring &&rhs){
    if (this == &rhs)
        return *this;
    delete [] str;
    str = rhs.str;
    rhs.str = nullptr;
    return *this;
}