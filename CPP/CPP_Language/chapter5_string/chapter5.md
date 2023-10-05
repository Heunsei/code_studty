# char and string
- char function
```cpp
#include <cctype>
function_name(char)
```
- isalpha > 영어
- isalnum > 영문 또는 숫자
- isdigit > 숫자
- islower > 소문자
- isprint > 출력가능한지 확인
- ispunct
- isupper > 대문자
- isspace > whitespace인지
- tolower > 소문자로
- toupper > 대문자로
- strlen > size_t를 반환 > 정수가 아님

# C - style string
- char의 연속
- constance > 불변
- 마지막을 null로 확인
- 연속된 데이터의 마지막이 null을 넣고 그것으로 끝을 판별하기 때문에
마지막에 값을 넣는다면 문제가 생길 가능성이 있음
- 빈 문자열 char my_name[8];을 선언 후 my_name = "Frank" 이런식으로 넣으면 에러발생
- > strcpy(my_name, "Frank"); 이것을 사용 해야함
- 문자열의 마지막이 null인지 확인이 필요함

# include<cstring>
- copying
- concatenation (문자열 더하기)
- comparison 
- searching
- and other

# C++ style string
- #include<string>
- std namespace
- dynamic size
- work with input and output streams
- operator (+, =, <, <=, >, >=) can be used

## declaring
- string s1;              //empty
- string s2 {"Frank"};
- string s3 {s2};
- string s4 {"Frank", 3};  // Fra
- string s5 {s3, 0, 2};   // 0으로부터 두개

## assignment
- string s1;
- s1 = "C++ Rocks!";
- stirng s2 {"Hello"};
- s2 = s1

## concatenation
- string part1 {"C++"};
- string part2 {"is a powerful"};
- string sentence;
- sentence = part1 + " " + part2 + " language";
- sentence = "C++" + " is powerful:; // Illegal

## accessing
- [] and at() method

## substr
- 문자열의 일부를 return
- pos 부터 count 길이 만큼의 문자열을 return

## string.find
- 문자열 에서의 str의 위치를 리턴
- string s1 = {"This is a test"};
- cout << s1.find("This"); // 0
- cout << s1.find("is"); // 2
- cout << s1.find("XX"); // std::npos

## string.erase() or clear()

## string.length()

# getline(cin, str_name, 'delim')
- 종결문자까지 문자를 읽어옴 없으면 \n으로 인식
- or cin.getline(char * str, streamsize n, char delim);
