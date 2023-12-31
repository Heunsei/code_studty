### 멤버 기본값
```cpp
class complex
{   
    public:
      complex(double r, double i) : r{r},i{i}
      {

      }
}
// 멤버변수를 선언과 함께 기본값으로 초기화 하는것
```

# **의미 이동론**
- 얕은 복사와 깊은복사
### 1. 얕은 복사
- 데이터 자체는 복사하지 않고 데이터의 주소만 복사하는 것이 얕은복사

### 2. 깊은 복사
- 데이터를 모두 복사해서 새로운 주소값에 저장, 프로그래머가 신경쓸 것이 적지만, 복사비용이 크기때문에 큰 객체를 함수가 돌려주는 상황에서 비효율적임.

### 3. 의미 이동론
1. 변수(명명된 항목 또는 '왼값')는 깊게 복사되지만, 임시 객체(이름으로 지칭할 수 없는 객체)는 데이터가 한 곳에서 다른 곳으로 옮겨질 뿐이란 것.
2. 임시 객체는 r-value에 해당, 오른값 참조는 &&로 지정
   즉, l-value, 명명된 항목은 오른값 참조로 전달할 수 없다

### 4. 이동 생성자
- 클래스에 이동 생성자와 이동 배정 연산자를 정의하면 오른값이 불필요하게 복사되는일을 방지가능.
```cpp
class vector
{
  // 이동 생성자
  vector(vector&& c) noexcept
    : my_size{v.my_size, data{v.data}}
  {
    // 이동 연산 이후에는 원시 포인터를 nullptr로 설정
    v.data = nullptr;
    v.my_size = 0;
  }
};
```
- 이동 생성자는 원본 객체로부터 데이터를 훔쳐온다.원본 객체는 빈 상태가 된다. 
- 오른값으로써 함수에 전달된 객체는 함수가 반환되면 만료 중 상태로 간주된다, 객체가 만료중이라는 것은
객체의 데이터 무결성이 더이상 보장되지 않는다는 뜻.
- 이동된 객체의 요구조건은 그 객체의 파괴가 절대로 실패하지 않아야 한다. 이동된 객체의 포인터가 엉뚱한 곳을 가리켜서 해제가 실패하거나 다른 어떤 데이터가 해제되는 일이 일어나서는 안된다.
- vecto&& c 같은 오른값 참조는 오른값이 아니다, v라는 이름이 있으므로 왼값이다.

### 5. 이동 배정 연산자
```cpp
class vector
{
  vector& operator=(vector&& src)
  {
    // assert 디버깅 모드에서 오류가 생기면 치명적일 곳이란곳에 심어두는 에러검출용 코드
    assert(my_size == 0 || my_size == src.my_size);
    std::swap(data, src.data);
    std::swap(my_size, src.my_size);
    return *this;
  }
}
```
- 객체 자신의 포인터를 이동된 객체의 포인터와 맞바꾸기 때문에 원래 가지고있던 데이터의 해제는 더 이상 신경쓰지 않아도 됨, 이동된 원본 객체의 소멸자에서 자동으로 해제

# 이동 의미론이 필요한 이유
- 이동 생성자는 새 객체를 생성하는 과정에서 왼값을 오른값으로 반환할 때 꼭 필요하다. 이런 변환을 통해 std::move 함수가 표준에 도입되었다. 이 함수는 주어진 객체를 오른값 참조로 변환한다. 함수 자체가 데이터를 이동시키지는 않음. 주어진 객체를 임시객체로 선언해서, 객체를 다른 함수로 이동할 수 있게 만드는것.
```cpp
vector x(std::move(w)); // x > 가 w의 데이터를 훔쳐 w를 빈 벡터로 만듬
v = std::move(u); // v와 u를 서로 교환
```
```cpp
class vector
{
  vector& operator=(vector&& src) noexcept
  {
    assert(my_size == 0 || my_size == src.my_size);
    delete[] data;
    data=src.data;
    // 이동 연산이 원본을 빈 상태로 만들어야함
    src.data= nullptr;
    src.my_size=0;
    return *this
  }
}
```
- 만료중인 객체는 파괴가 되지 않았을 뿐 실용적인 의미는 사라진 상태라고 할 수 있다.
- 의미 이동론의 개념은 연산이 수행된 직후 사라질 임 객체로부터 데이터를 훔친다는것
- 만료중인 객체를 잘 관리할 필요가있음. 이동된 객체(만료된 객체)에는 더이상 접근하지 않아야 한다.
- 이동된 데이터가 전역 변수나 함수 또는 클래스의 static 변수일 수있는데, 그런 변수는 프로그램이 끝날때 까지 살아남고, c++에는 그런 만료 중 객체를 함수에서 함수로 전달할 수 못하게 금지하는 기능이없음
- 따라서 생성 시점에서부터 변수의 수명을 일일이 추적해서 변수가 쓰이는 실행 경로중에 move가 명시적으로 적용되는 곳이 있는지 확인해야 한다.

# 오른값을 다루는 방식
1. 완전양도 : 동적으로 관리되는 자원들만 가진 클래스는 자원들을 한 객체에서 다른 객체로 완전히 넘겨줄수 있다, unique_ptr는 참고된 메모리를 한 객체에서 다른 객체로 완전히 넘겨준다
2. 복사 : 동적 자원이 없는 클래스는 자신의 내용을 복사하기만 한다. 이런 클래스는 이동 생성자와 이동 배정 연산자를 아예 제공하지 않을 때가 많다
3. 내부양도 : 내용을 완전히 넘겨주는것이 불가능 하지만, 개별 요소는 넘겨줄 수 있음
4. 부분양도
5. 선택적 양도

- 동적 자원을 다룰 때는 완정 양도가 가장 효율적인 이동 방식이다.
- 동적 자원을 완전히 넘겨줄 때는, 이동의 원본을 빈 상태로 남겨두는 것이 자연스럽다.

# 소멸자
- 객체가 파괴될 때 호출되는 함수
## 구현 규칙
## 1.소멸자 바깥으로 예외를 던져서는 안됨, 소멸자 또는 소멸자가 호출한 함수에서 발생한 예외는 반드시 소멸자 안에서 잡아서 처리해야함
## 2.클래스에 virtual함수가 있으면 소멸자도 반드시 virtual이어야함

# 매소드 생성 요약
## 자동으로 생성되는 6대 메소드
1. 기본 생성자
2. 복사 생성자 
3. 이동 생성자
4. 복사 배정 연산자
5. 이동 배정 연산자
6. 소멸자

# 2.6.4 참조 한정 멤버
- const로 객체의 상수성을 지정하는 것과 함께 현재 객체가 왼값 참조인지 오른값 참조인지도 지정 가능
- 배정 연산의 좌변에는 오직 가변 왼값만 와야한다. 사용자 형식에서는 참조 한정자를 명시해줘야함
```cpp
vector& operator=(const vector& src)& {...} // & 참조 한정자
```
- 배정 연산의 좌변에 가면 왼값만 올 수 있다
