# 연산자 오버로딩
- 연산자들을 유저정의 형식으로 재정의 하는것
- 자세한 구현들은 source 파일 안에

- move assignment operator
- 정의 안되어 있으면 기본적으로 복사 생성자 사용
- 정의 하는데 오래 안걸리니까 정의하라네요
```cpp
Type &Type::operator=(Type &&rhs);
```
- 복사 생성자와 마찬가지로 재할당 할때는 이전에있던 저장값을 deallocate하고 저장값을 새로 확보한뒤 저장

# 오버로딩에서의 const 역할
```cpp
const Point operator+(const Point& target) const
{
	Point ret;
	ret.x = this->x + target.x;
	ret.y = this->y + target.y;
	return ret;
}
```
- 1. 함수 이름 앞의 const는 A+B 에 대한 결과물인 임시객체가 C로 할당되기 전까지 변하지 않는다 라는 뜻
- 2. parameter 앞의 const는 피연산자에 대한 정의 B 가 변하지 않는다는 의미
- 3. 함수 뒤 const는 클래스 내부에서 유효한 것, 객체 A에 대한 정의 this로 통하는 모든 변수는 함수 내에서 수정불가 > 이 함수는 멤버 변수의 값을 수정하지 않음

```cpp
Mystring Mystring::operator-() const{
  char *cuff = new char[std::strlen(str)+1]
  std::strcpy(buff, str);
  for(size_t i = 0; i<std::strlen(buff); i++)
    buff[i] = std::tolower(buff[i]);
  Mystring temp {buff};
  delete[] buff;
  return temp;
}
```
# == operator

```cpp
bool Mystring::operator==(const Mystring &rhs) const{
  if(std::strcmp(str, rhs.str)==0)
    return true;
  else
    return false;
}
```
# + operator
```cpp
Mystring Mystring::operator+(const Mystring &rhs) const{
  size_t buff size = std::strlen(str) + 
                     std::strlen(rhs.str) + 1;
  char *buff = new char[buff_size];
  std::strcpy(buff, str);
  std::strcat(buff, rhs.str);
  Mystring temp {buff};
  delete[] buff;
  return temp;
}
```

# 프렌드로 연산자 오버로딩
```cpp
// 클래스 안에서 선언할 것, member 오퍼레이터가 아니니까 인자값을 확실히 설정해야함
friend bool operator ==(const Mysting &lhs, const Mystring &rhs);
friend bool operator -(const Mysting &obj);
friend bool operator +(const Mystring &lhs, const Mystring &rhs);
```
```cpp
// member function이 아니라 global임
bool operator==(const Mystring &lhs, const Mystring &rhs){
  return (std::strcmp(lhs.str, rhs.str) == 0); 
}

Mystring operator-(const Mystring &obj){
  char *buff = new char[std::strlen(obj.str) + 1];
  std::strcpy(buff, obj.str);
  for(size_t i=0; i<std::strlen(buff);i++)
    buff[i] = std::tolower(buff[i]);
  Mystring temp {buff};
  delete[] buff;
  return temp;
}

Mystring operator+(const Mystring &lhs, const Mystring &rhs){
  char *buff = new char[std::strlen(lhs.str) + std::strlen(rhs.str) + 1];
  std::strcpy(buff, lhs.str);
  std::strcat(buff, rhs.str);

  Mystring temp{buff};
  delete [] buff;
  return temp;
}
```
# stream insertion and extraction
```cpp
std::ostream &operator<<(std::ostream &os, const Mystring &obj){
  os << obj.str;  // if friend function
  // os << obj.get_str() // if not friend function
  return os;
}

std::istream &operaotr>>(std::istream &is, Mystring &obj){
  char *buff = new char[1000];
  is >> buff;
  obj = Mystring{buff}; // If have copy or move assignment
  delete [] buff;
  return is
}
```