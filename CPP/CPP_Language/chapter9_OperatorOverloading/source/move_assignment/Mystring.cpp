#include <iostream>
#include <cstring>
#include "Mystring.h"

Mystring::Mystring()
  : str{nullptr}{
    str = new char[1];
    *str = '\0';
}

Mystring::Mystring(const char *s)
  :str {nullptr}{
    if(s==nullptr){
      str = new char[1];
      *str = '\0';
    }else{
      str = new char[strlen(s)+1];
      strcpy(str,s);
    }
}

Mystring::Mystring(const Mystring &source)
  :str{nullptr}{
    str = new char[strlen(source.str)+1];
    strcpy(str,source.str);
    std::cout << "copy constructor used" << std::endl;
}

Mystring::Mystring(Mystring &&source)
  : str{source.str}{
    source.str = nullptr;
    std::cout << "Move constructor used" << std::endl;
}

Mystring::~Mystring(){
  if(str==nullptr){
    std::cout << "calling destructor for mystring : nullptr" << std::endl;
  }else{
    std::cout << "calling destructor for Mystring" << endl;
  }
  delete[] str;
}

// 복사대입연산자
Mystring &Mystring::operator=(const Mystring &rhs){
  std::cout << "using copy assignment" << std::endl;
  if(this == &rhs)
    return *this;
  delete[] str;
  str = new char[strlen(rhs.str)+1];
  strcpy(str, rhs.str);
  return *this;
}

Mystring &Mystring::operator=(Mystring &&rhs){
  std::cout << "using move assignment" << std::endl;
  if(this == &rhs){
    return *this;
  }
  delete[] str;
  str = rhs.str;
  rhs.str = nullptr;
  return *this;
}

