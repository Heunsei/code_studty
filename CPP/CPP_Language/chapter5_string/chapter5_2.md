# Defalut Argument Values
- 인자가 전달되지 않았을 때, 컴파일러에게 디폴트 매개변수를 알려줌
- 프로토타입 함수에 주로 설정하는게 좋다
```cpp
// example
double calc_cost(double base_cost, double tax_rate = 0.06);
// 호출할때 입력 받으면 바뀐값을 사용하고 그게 아니면 0.06사용
```

# Function overloading
- 같은 이름으로 함수를 설정
- 타입에 대한 버전을 생성
```cpp
//example
int add_numbers(int, int);
double add_numbers(double, double);

int main(){
    cout << add_number(10,10) << endl;
    cout << add_number(10.5, 12.5) << endl;
}

int add_number(int a, int b){
    return a+b;
}

double add_number(double a, double b){
    return a+b;
}
```

# passing arrays to function
- void print_arr(int numbers []);
- array elements are NOT copied
- 주소가복사가 되어서 전달됨
- 따라서 컴파일러는 오직 배열의 시작점만 알기에 배열의 크기가 얼마나 큰지 모르므로 배열의 크기를 전달해주어야함
```cpp
int print_array(int numbers [], size_t size);
int main(){
    int my_numbers[] {1,2,3,4,5};
    print_array(my_numbers,5);
    return 0;
}
int print_array(int numbers [], size_t size){
    for (size_t i {0}; i < size; ++i){
        cout << numbers[i] << endl;
    }
}
```

# 참조
- 배열이나 벡터를 참조할때는 상수선언을 하고 참조후 돌려주는게 좋다
```cpp
//example 
void scale_num(int &num);
int main(){
    int number {1000};
    scale_num(number);
    cout << number << endl;
    return 0;
}
void scale_num(int &num){
    if (num>100)
        num = 100;
}
```
### swap
```cpp
//example 
void swap(int &a, int &b);
int main(){
    int x {10}, y{20};
    cout << x << " "<< y<< endl;
    swap(a,b)
    cout << x << " "<< y<< endl;
    return 0;
}
void swap(int &a, int &b){
    int tmp = a;
    a = b;
    b = tmp;
}
```