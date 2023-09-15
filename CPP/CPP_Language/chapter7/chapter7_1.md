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
- new keyword를 사용해 설정
```cpp
int *int_ptr {nullptr};
int_ptr = new int;        // heap에 integer를 올려둠
cout << int_ptr << endl;  // heap에 할당시켜둔 주소를 출력
cout << *int_ptr << endl; // garbage , 값이 할당 안되어있음
*int_ptr = 100;
cout << *int_ptr << endl; // 100 출력
delete int_ptr; // 다썻으면 지워야지? 
```
```cpp
int *arr_ptr {nullptr};
int size {};

cout << "How big do yo want the array?";
cin >> size;

arr_ptr = new int[size]; // allocate array on the heap
// size 만큼 int를 넣을 수 있는 길이의 연속된 메모리를 할당해둠
delete [] array_ptr;
```

# 배열과 포인터의 관계
- the value of an array name is the adress of the first element in the array
- the value of a pointer variable is an address
- if the pointer point to the same data type as the array element then the pointer and array name can be used interchangeably
```cpp
ins scores[] {100, 95, 89};
int *score_ptr {scores};

cout << score_ptr[0] << endl;   // 주소
cout << score_ptr[1] << endl;   // 주소
cout << score_ptr[2] << endl;  // 주소

cout << score_ptr << endl;      // 주소
cout << (score_ptr+1) << endl;  // 주소
cout << (score_ptr+1) << endl;  // 주소
```

# 포인터 산술 (pointer arithmetic)
- https://boycoding.tistory.com/202
- C++ 언어를 사용하면 포인터에서 정수 추가 또는 빼기 작업을 수행할 수 있다. 만약 ptr이 정수를 가리키면 ptr+1은 ptr 다음 메모리의 정수 주소가 된다. ptr-1은 ptr 이전 정수의 주소다.

- ptr+1은 ptr 뒤 메모리 주소를 반환하지 않고 ptr이 가리키는 객체의 다음 메모리 주소를 반환한다. ptr이 정수 (4바이트라고 가정)를 가리키면, ptr+3은 ptr 이후에 3개의 정수 (12바이트)를 의미한다. ptr이 항상 1바이트인 char을 가리키면, ptr+3은 ptr이후에 3개의 문자(3바이트)를 의미한다.

- int_ptr++ or -- 가능

```cpp
string s1 {"Frank"};
string s2 {"Frank"};

string *p1 {&s1};
string *p2 {&s2};
string *p3 {&s1};
// *을붙이면 값을 비교하는 것이므로 둘다 true로 나옴
cout << (p1 == p2) << endl; // 값은 같으나 서로 다른 주소를 가르킴
cout << (p1 == p3) << endl; // True
```

# 상수를 가리키는 포인터 - const int *ptr
- 포인터가 가리키는 대상을 상수화, 변수가 상수가 아니더라도 상수로 취급한다
- 주소는 변경이 가능하지만 포인터로 접근해 값을 직접 변경하는것은 불가능하다
- 함수의 파라미터에서 실수로 배열을 변경하지 못하도록 할때 사용
```cpp
int high_score {100};
int low_score {50};
const int *score_ptr {&high_score};
*score_ptr = 86; // 주소에 접근해 값을 변경한다 > error
score_ptr = &low_score; // ptr의 주소를 low_socre의 주소로 변경 okay
```

# 상수 포인터 - ins const * ptr
- const 키워드를 사용해 포인터 자체를 상수화 시킴
- 포인터가 상수화 되었기에 주소는 변경이 불가능하지만 주소안에 들어있는 값을 변경하는것은 가능하다
```cpp
int a {100};
int b {200};
int *const ptr {&a}; // 상수 포인터 ptr에 a의 주소를 넣어줌
ptr = &b; // ptr에 b의 주소를 지시하도록 한다 > error
*ptr = 300; // ptr안에있는 값을 변경한다
```

# 상수를 가리키는 상수 포인터 - const int *const ptr
- 위의 두 개념을 모두 합친 포인터

