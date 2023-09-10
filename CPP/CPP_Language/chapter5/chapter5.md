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