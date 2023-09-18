# 함수에 포인터를 전달
- 포인터를 전달한다 생각하지말고
- 주소값을 넣어준다고 생각하자
```cpp
void double_data(int *int_ptr);
void double_data(int *int_ptr){
  *int_ptr *= 2;
}
```
```cpp
int main(){
  int value {10};
  cout << value << endl;  //10
  double_data(&value); // &는 주소값
  cout << value << endl;  //20
}
```

# 함수로 포인터를 반환
- type *function();
- 결과값을 저장하는 변수는 포인터형식
```cpp
int *largest_int(int *int_ptr1, int *int_ptr2){
  if (*int_ptr1 > *int_ptr2)
    return int_ptr1;
  else
    reutnr int_ptr2;
}
```
```cpp
int *create_array(size_t size, int init_value = 0){
  int *new_storage {nullptr};
  // new_storage를 시작으로 int를 저장할수있는 메모리를 size만큼 할당
  new_storage = new int[size]
  for (size_t i {0}; i < size; ++i)
    *(new_storage + i) = init_value;
  // 동적으로 할당한 배열의 첫번째 주소를 반환
  return new_storage;
}
```
- don't do this
```cpp
// size는 local 변수임 이걸 밖으로 내보냈다간 무슨일이 일어날지 모름
// 함수에서 로컬변수의 주소를 반환 하면, 스택에 있던 변수는 함수가 종료함에따라 수명이 다함. 그 후 다른 함수가 호출되거나, 어느 다른 함수가 호출 될 때 스택 영역이 재사용될것이고, 그때 다른 함수의 영역을 건드릴 수 있음
// 흔히 말한다는 포인터가 터진다라는 뜻
int *first(){
  int size {};
  return &size;
}

int *second(){
  int size {};
  int *int_ptr {&size};
  
  return int_ptr;
}
```

# C++에서 함수 내에서 생성한 로컬 데이터의 주소를 반환하면 안되는 이유
- 1. 수명 문제:
  - 로컬 변수는 함수가 호출될 때 생성되고, 함수가 종료될 때 파괴. 따라서 함수 내에서 생성된 로컬 변수의 주소를 반환하면, 함수가 종료되면 해당 변수는 스택에서 제거되어 더 이상 유효하지 않은 메모리 주소를 가리키게 됨. 이로 인해 다른 부분에서 이 주소를 사용하려고 하면 예측할 수 없는 동작 또는 프로그램 충돌이 발생할 수 있다.
- 2. 스택 메모리의 재사용:
  - 로컬 변수가 사용한 스택 메모리는 함수가 호출될 때 스택 프레임에 할당되고, 함수가 종료되면 이 스택 메모리는 다른 함수 호출에 사용 가능. 따라서 함수가 종료된 후에 반환된 주소가 다른 변수나 데이터를 가리킬 수 있으므로 오류가 발생가능.
- 3. 복사 대신 포인터를 사용
  - 함수 내에서 로컬 변수의 값을 반환하는 대신 로컬 변수의 값을 복사하거나, 동적메모리 할당을 통해 메모리를 할당하고 그 메모리 주소를 반환하는것이 안전.
  함수내에서 동적으로 메모리를 할당하고 주소를 반환하면, 해당 메모리는 함수의 수명과 상관없이 살아있음.
# 포인터를 쓸 때 중요한 점
- 초기화 되었는지 확인
  - int *int_ptr;
  - int *int_ptr {null_ptr};
- Dangling pointer
  - 포인터가 여전히 해제된 메모리 영역을 가리키고 있을때
  - 메모리 접근시 예측 불가능한 동작
  - 메모리 접근 불가시 sementations falut
  - 잠재적인 보안위험 발생
  - 메모리를 해제후 포인터를 NULL 로설정하자
- memory leak
  - 메모리 해제를 까먹었을 때
  
# 참조
- 선언된 자료를 사용할때 우리는 원본을 사용하는것이 아니라 원본을 복사한 자료를 수정해서 사용함
- &을 사용해 원본에 접근

# L-value, R-value
- l-value
  - values that have name and addressable
  - modifiable if they are not constants
- r-value
  - right side of an assignment expression
  - literal