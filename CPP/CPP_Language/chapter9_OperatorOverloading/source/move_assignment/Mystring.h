#ifndef _MYSTRING_H_
#define _MYSTRING_H_

class Mystring
{
private:
  char *str;
public:
  Mystring();
  Mystring(const char *c);          // 생성자 오버로딩
  Mystring(const Mystring &socure); // 복사 생성자
  Mystring(Mystring &&source);      // 이동 생성자
  ~Mystring();                      // 파괴자

  Mystring &operator=(const Mystring &rhs);
  Mystring &operator=(Mystring &&rhs);

  void display() const;

  int get_length() const;
  const char *get_str() const;
};
#endif