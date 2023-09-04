# 일반적 프로그래밍
- 템플릿은 매개변수적 형식이라고도 부르는 일반적 형식들에 대해 작동하는 함수와 클래스를 만드는 데 쓰이는 기능이다.
- 일반적 프로그래밍은 정확성을 유지하면서 최대한의 적용성을 추구하는 프로그래밍 패러다임

## 3.1 함수 템플릿
- 함수 템플릿은 잠재적으로 무한히 많은 함수 중복적재 버전을 생성할 수 있는 하나의 청사진.
```cpp
template <typename T>
T max (T a, T b)
{
    if (a>b)
        return a;
    else 
        return b;
}
```
- 템플릿으로부터 구체적인 인스턴스가 만들어지는 것을 템플릿 인스턴스화 라고 부른다.

### 3.1.1 템플릿 인스턴스화
- 템플릿 오류는 형식 매개변수에 대입된 실제 형식과 관련된다,템플릿 함수 그 자체로는 오류가 없지만,구체적인 형식으로 인스턴화하는 시점에 오류가 발생 가능
- 멤버변수가 없는 형식을 사용할때 일어나는 오류가 발생가능
- 어떤건 멤버변수를 지원하는데 다른건 아닐때

### 3.1.2 형식 매개변수의 연역
- 3.1.2.1
```cpp
// const 나 &가 붙거나 붙지 않은 모든 가능한 조합을 대표하는 패턴
template <typename TPara>
void f1(Tpara p);

int main()
{
    int i = 0;
    int& j = i  // 가변 참조 변수
    const int& k = i; // 상수 참조 변수

    f1(3);
    f1(i);
    f1(j);
    f1(k);
    //호출에서 Tpara는 모두 int로 치환
}
```

- 3.1.2.2
1. 매개변수를 상수 참조로 선언하면 모든 인수를 받을 수 있다.
```cpp
// Tpara에서 인수의 형식에서 모든 한정사를 제거한 것
template <Typename TPara>
void f2(const TPara& p) {}
``` 
```cpp
// 모든 리터럴과 임시 객체를 거부
template <Typename TPara>
void f2(TPara& p) {}
``` 
- 3.1.2.3 전달 참조
1. T&& 형태의 매개변수는 오른값뿐만 아니라 왼값도 받는다
```cpp
template <Typename Tpara>
void f4(Tpara&& p) {}

f4(3);
f4(move(i));
f4(move(up));
```
2. 왼값으로 f4를 호출하면 컴파일러는 그러한 인수를 템플릿 오른값 참조 매개변수로 받아들인다
3. 인수 형식과 템플릿 매개변수 중 적어도 하나가 왼값 참조이면 축약결과는 왼값 참조이다

### 3.1.3 간단한 템플릿 매개변수 c++20이상
- 함수 매개변수를 auto로 선언하면 그 함수는 자동으로 템플릿 함수가 된다
```cpp
auto mas(auto a, auto b)
{
    return a > b ? a : b;
}
```

## 3.2 이름공간과 함수 조회

### 3.2.1 namespace
- 이름공간은 min이나 max, abs같은 이름들을 여러 문맥에서 정의할 수 있게 하는 수단
- 이름공간이 없으면 서로 다른 문맥의 같은 이름들이 충돌해서 중의성 문제를 일으키기 쉽다.
- namespace의 위계구조 의 특정 이름을 using 선언문을 이용해 현재 범위에 도입하면 이름공간 한정 없이 해당 이름만 간결하게 표기 가능
- 안쪽 범위에서 함수를 선언하거나 정의하면 그 함수와 서명이 같은 바깥쪽 함수 중복적재 버전만 가려지는게 아니라 모든 함수 중복적재 버전이 가려진다, 즉 이름 가리기는 특정 중복적재 버전이 아니라 '이름' 자체를 가려버린다
- 안쪽 범위에서 함수가 아니라 클래스나 변수의 이름을 f 로 선언해도 전역함수 f 가 가려진다. f 를 호출하려면 using 선언으로 전역f 를 현재 범위에 도입해야한다.
- 이름 하나를 도입할 떄처럼 이름공간 도입도 함수나 이름공간 안에서만 가능하고 클래스 안에서는 불가능하다
- using namespace std 같은 문장으로 표준 이름공간을 도입할때, main함수 첫행에 두거나 소스파일에서 include 지시문 다음에 두기도 하는데
전역 공간에 std 이름공간을 도입하면 vector라는 클래스를 전역적으로 정의할 때 std::vector와 충돌 할 수 있다.
- 헤더파일 안에서는 (함수정의 바깥에서) 이름이나 이름공간을 도입하지 말자

### 3.2.2 인수 의존적 조회 (ADL)
- 함수 이름을 현재 이름공간뿐만 아니라 인수들의 이름공간에서도 찾는것을 말한다.
- 단, 인수 이름공간들의 부모 이름공간까지 검색을 확장하지는 않는다

## 3.3 클래스 템플릿
- 클래스 템플릿은 벡터나 행렬, 목록 같은 범용 컨테이너 클래스를 만들때 유용

### 3.3.1 컨테이너 예제
- 선형대수의 벡터를 클래스로 만들어보자
```cpp
template <typename T>
class vector
{
    public: 
      explict vector(int size)
        : my_size{size}, data{new T[my_size]}
      {}
      
      vector(const vector& taht)
        : my_size{that.my_size}, data{new T[my_size]}
      {
        std::copy(&that.data[0], &that.data[that.my_size], &data[0]);
      }

      int size() const {return my_size}

      const T& operator[](int i) const
      {
        check_index(i);
        return data[i];
      }
    private:
      int my_size;
      std::unique_ptr<T[]> data
}
```
- 멤버들의 형식을 지정하는데 쓰이는 여분의 형식매개변수 T가 있을뿐 근본적으로 보통의 클래스 선언과 다르지 않다

### 3.4.2 decltype
- 명시적인 형식이 필요하지만 auto를 사용할 수 없을 때 중요함
```cpp
// 덧셈 연산자가 두 벡터들의 첫 요소들의 합을 돌려준다 할때 그 연산자의
// 반환형은 두 벡터의 요소를 합을 온전히 담을 수 있는 v1[0] + v2[0]이어야한다
template <typename Vector1, typename Vector2>
auto operator+(const Vector1& v1, const Vector2& v2)
 -> vector<decltype(v1[0] + v2[0]) >;
 // 후행 반환 형식
 // 함수 이름 앞에 v1과 v2가 선언되지 않았기 때문에 반환식에 v1[0] + v2[0]
 // 라고 쓸 수 없기 때문에 표현식이 유효해지지 않음
```

### 3.4.3 decltype(auto)
- decltype(expr) = expr;
- decltype(auto) = expr;
- 반환 형식을 연역할때 한정사들을 유지하는것이 중요함
- 요청된 벡터 요소가 특정 범위에 속하는지 판정하는 벡터 뷰를 만든다 할때 이 뷰의 operator[]은 지정된 요소가 범위에 속한다면 요소를 돌려줘야 하는데, 이때 반환 형식은 원래의 벡터요소에 적용된 한정사를 모두 유지해야함

### 3.4.6 형식 정의
- 형식을 정의하는 수단 typedef, using
- typedef double value_type; > 새 이름이 오른쪽
- using value_type = double > 새 이름이 왼쪽

## 3.5 템플릿 특수화