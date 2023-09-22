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

```cpp
bool Mystring::operator==(const Mystring &rhs) const{
  if(std::strcmp(str, rhs.str)==0)
    return true;
  else
    return false;
}
```