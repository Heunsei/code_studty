#ifndef _MYSTRING_H_
#define _MYSTRING_H_

class Mystring
{
    friend std::ostream &operator<<(std::ostream &os, const Mystring &rhs);
    friend std::istream &operator>>(std::istream &in, Mystring &rhs);
private:
    char *str;
public:
    Mystring();                         // 기본 생성자
    Mystring(const char*s);             // 생성자
    Mystring(const Mystring &source);   // 복사 생성자
    Mystring(Mystring &&source);        // 이동 생성자
    ~Mystring();                        // 파괴자

    Mystring &operator=(const Mystring &rhs); // 복사 할당자
    Mystring &operator=(Mystring &&rhs);      // 이동 할당자

    void display() const;

    int get_length() const;
    const char *get_str() const;
};
#endif