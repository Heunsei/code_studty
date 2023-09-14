# Pointer
- 형식과 값을 가진 value
- 값은 메모리의 주소
- 포인터는 변수나 함수를 가르킴
- 함수 내에서 사용할 복사본의 주소를 가르키는 방법등으로 사용

## 1. Declaring pointers
- vairalbe_type *pointer_name {nullptr};
- int *int_ptr {};
- double *double_ptr {nullptr};

## 2. accessing pointer adress
- 주소연산자 &를 사용해 주소에 직접 연결 가능
- int num{10}; 등으로 초기화한 변수에 &num을 출력시키면 주소값이 나옴
```cpp
int *p;
cout << p << endl; // garbage
cout << &p << endl; // 주소출력
p = nullptr;
cout << p << endl; // 0
```
```cpp
int score {10};
double high_temp {100.7};
int *score_ptr = {nullptr};
score_ptr = &score;
score_ptr = &high_temp; // compiler error
```
- 포인터도 결국 변수이기 때문에 값을 바꿀수있음
```cpp
double high {};
double low {};
double *temp_ptr;
temp_ptr = &high;
temp_ptr = &low;
temp_ptr = nullptr;
// 각각 의 대입마다 ptr의 값이 변함
```

# Dereferencing 역참조
```cpp
int score {100};
int *score_ptr {&score};
cout << *score_ptr << endl; // 100

*score_ptr = 200;
cout << *score_ptr << endl; // 200
cout << score << endl; //200
```

# dynamic memory allocation
- 동적 메모리 할당