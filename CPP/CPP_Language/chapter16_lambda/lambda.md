# 람다 표현식
- [] (매개변수) { // 함수 동작 } (호출 시 인자) ; 
[캡처] (매개변수) { 함수 동작 } (호출인자)

- 1. 매개변수가 없는 람다 표현식 
    : [] {cout << exp << endl;};
- 2. 매개변수가 있는 람다 표현식
    : [] (int a, int b, int c) { cout << a << b << c << endl;};
- 3. 매개변수가 없고 반환을 하는 람다
    : [] { return 1234; };
- 4. 매개변수가 있고 반환도 하는 람다
    : [] (int a, int b) { return a + b;};

- 캡쳐 구문 사용법
- [result1, result2] () {} ()
    - 변수 result1, result2를 복사해서 람다 함수 내부에서 사용
- [&result1, &result2] () {} () 
    -  변수 result1, result2 를 참조해서 람다 함수 내부에서 사용
- [result3, &result4] () {} () 
    - 변수 result3은 복사 result4는 참조해서 람다 함수 내부에서 사용
- [=] () {} () 
    - 모든 외부 변수 result1, result2, result3, result4를 복사해서 람다 함수 내부에서 사용
- [&] () {} () 
    - 모든 외부 변수 result1, result2, result3, result4 를 참조해서 람다 함수 내부에서 사용
- [&, result3] () {} () 
    - 모든 외부 변수 (result1,2,4)은 참조로 사용하지만, result3만 복사로 사용
- [=, &result3] () {} ()
    - 모든 외부 변수 (result1,2,4)은 복사로 사용하지만, result3만 참조로 사용