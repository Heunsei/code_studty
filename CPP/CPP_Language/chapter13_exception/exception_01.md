# 예외처리
- Syntax
- 1. throw
    - 예외발생 시 예외 제시
- 2. try{ }
    - 던져진 예외는 catch handler에 의해 처리됨
    - catch handler가 없을면 프로그램은 종료됨
- 3. catch(Exception ex_) { }
    - 예외처리를 하는 코드
    - 여러개의 catch handlers를 포함 가능
    - 프로그램을 종료시킬수도 그렇지 않을 수도 있다
     
## stack unwinding
- 함수안에서 함수를 call 하는 경우 맨 위의 함수(스택에서)에서 오류가 발생한 경우 catch를 찾아 뒤의 절차는 무시하고 함수 밖으로 튀어나올 수 있음

## user defined exception class
```cpp
class DivideByZeroException{
};
class NegativeValueException{
};
double calculate_mpg(int miles, int gallons){
    if(gallons == 0 ) throw DivideByzeroExcption();
    if (miles<0 || gallons<0) throw NegativeValueExcption();
    return static_cast<double>(miles) / gallons;
}
```

## Class level exceptions
```cpp
Account::Account(std::string name, double balance) 
    : name{name}, balance{balance}{
        if (balance < 0.0) throw IllegalBalance(); 
    }
```