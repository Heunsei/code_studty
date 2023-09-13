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