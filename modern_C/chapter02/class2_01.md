# 클래스
## 멤버
- 데이터 : 멤버 변수라고도 칭함.전통적으로 필드라고도 불림
- 함수 : Methods 또는 member function
- 형식정의, 내부 클래스

### 멤버 변수 선언
```cpp
class complex
{
    public:
        double r, i;
};

complex z,c;
z.r = 3.5; z.i = 2;
c.r = 2; -3.5;
std::cout << " z is ("<< z.r <<", " << z.i <<")\n";
```

### 접근성
- c++에서는 클래스의 각 멤버에 접근성이 세종류 존재
- **public** 멤버 어디서든 접근 가능
- **private** 해당 클래스 안에서만 접근 가능
- **protect** 클래스 자신과 파생 클래스에서 접근 가능
- 클래스 멤버의 접근성은 접근 수정자로 제어
```cpp
class rational
//기본적으로 class 멤버의 접근성은 private
{
    public:
        rational operator+{}
        rational operator-{}
    private:
        int q;
        int p;
}
```

```cpp
struct xyz
//기본적으로 struct 멤버의 접근성은 public
{

}
```
## 새로운 추상은 class로 정의하고, 기능이 제한적이고 데이터중심은 struct로 정의

### friend 함수
- 특정한 외부 함수나, 클래스를 그 클래스의 친구로 선언하면 그 함수나 클래스는 클래스의 private 멤버들과 protected멤버에 접근할 수 있다.

```cpp
class complex
{
    friend calss complex_algebra;
    // calss complex_algebra를 friend로 선언
    // 이 클래스는 complex의 private, protected멤버에 접근가능
}
```

### 접근 연산자
```cpp
{

    complex c;
    complex* p = &c;

    *p.r=3.5; 오류 *(p.r)로 해석됨
    (*p).r = 3.5;

    p -> r =3.5 //이런 식으로도 가능
}
```

### 정적 멤버 선언
1. static으로 선언된 정적 멤버 변수는 클래스당 하나만 존재
2. 정적 멤버 변수는 단일체 또는 싱글톤을 구현하는데 사용
3. static과 함께 const로 선언된 데이터 멤버는 클래스당 하나만 존재하며 수정할 수 없다
4. 메소드도 static으로 선언 가능.정적 데이터 멤버에만 접근 가능하고 정적메소드만 호출 가능(외부 함수,변수에 대해서는 일반적 접근과 가시성 규칙 적용)

### 멤버 함수
```cpp
class complex
{
    public:
        double get_r(){return r;}
        void set_r(double newr){r = newr;}
        double get_i(){return i;}
        double set_i(double newi){i = newi;}
}
```

# 생성자
- 클래스의 객체를 생성하는 특별한 메소드
- 생성자는 데이터 멤버를 초기화 하고, 멤버 함수들의 작업환경을 만든다
```cpp
class complex
{
    public:
        complex(double rnew, double inew)
        {
            r = rnew; i = inew;
        }
}
```
- 생성자는 클래스 자체ㅐ와 같은 이름의 멤버 함수
- 반환 형식이 없으며 임의의 개수와 형식의 매개변수를 받아 올 수 있다.
```cpp
class complex
{
    // 멤버 초기화 목록
    public:
      complex(double rnew, double inew)
      : r(rnew),
        i(inew)
      {}
    // 초기화 목록에 멤버들이 나열된 순서는 클래스 선언 안에서 멤버들이 선언된
    // 순서와 반드시 일치헤야함
}
```
## 기본생성자
- 매개변수가 없거나 모든 매개변수에 기본값이 선언된 생성자
- 내부 범위에서 초기화되는 변수가 알고리즘상의 이유로 외부에서도 유효해야 하는 경우, 의미 없는 값으로 **변수를 초기화** 해야함.
-기본 생성자가 없는 형식에 대해서는 컨테이너를 구현하기가 번거로워짐

## 복사생성자
- 객체가 명시적으로 복사되는 방법을 지정
```cpp
class complex
{
    public:
    complex(const complex& c) :r{c.r}, i{c,i} {}
}
int main()
{
    complex z1(3.0, 2.0_),
            z2(z1) // 복사
}
```
- 컴파일러가 복사생성자를 대부분 만들어주지만 혹시 의심스러울때
- complex(const complex& c) = dafault;
- 거의 모든경우에서 복사 생성자의 인수는 상수 참조로 전달
- 포인터 변수를 그대로 복사하는 방식으로 백터 객체를 복사하면 복사한 모든 객체가 같은 메모리 블록을 가르키게 된다.

### 변환과 명시적 생성자
- c++은 암묵적 생성자와 명시적 생성자를 구분.
- 암묵적 생성자는 암묵적 변환을 활성화하며, 배정연산과 비슷한 표기법으로 객체를 생성하는 구문 허용

```cpp
// 이런 구문 대신
complex c1{3.0}; 
complex c1(3.0);
//다음 구문이나
complex c1 = 3.0;
// 다음 구문 사용 가능
complex c1 = pi * pi / 6.0;
// 암묵적 변환이 일어나지 않게 하려면
//explcit 키워드사용
```