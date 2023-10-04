#ifndef _MYSTRING_H_
#define _MYSTRING_H_

class Mystring
{
    friend std::ostream &operator<<(std::ostream &os, const Mystring &rhs);
    friend std::istream &operator>>(std::istream &os, Mystring &rhs);

private:
    char *str; // 문자열 배열을 지시하는 포인터
public:
    Mystring();                                 // 생성자
    Mystring(const char *s);                    // 생성자 오버로딩
    Mystring(const Mystring &source);           // 복사생성자
    Mystring(Mystring &&source);                // 이동생성자
    ~Mystring();                                // 파괴자

    Mystring &operator=(const Mystring &rhs);   // 복사대입자
    Mystring &operator=(Mystring &&rhs);        // 이동대입자

    void display()  const;

    int get_lenght()  const;
    const char *getstr()  const;
};

#endif