## operator ==
```cpp
bool Mystring::operator==(const Mystring &rhs) const{
    // std::string compare
    if(std::strcmp(str, rhs.str)==0)
        return true;
    else
        return false;
}
```