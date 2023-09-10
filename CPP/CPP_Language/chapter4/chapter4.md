# 조건문
- if statement
```cpp
if (expr){
    statement;
}
```

# 조건 연산자
- (cond_expr) ? expr1 : expr2
- trye 면 앞, false면 뒤 반환

# rangebase loop
```c++
for (val_type var_name : sequence)
{
    statement
}
```

```cpp
int scores [] {100, 90 97};
// int 대신 auto 사용 가능
for (int score : scres)
{
    cout << score << endl;
}
```

```cpp
vector<double> temps {87.2, 77.1, 80.0, 72.5 };
double avg_tmp {};
double running_sum {};
for (doubel tmp : tmps)
    running_sum += tmp;
avg_tmp = running_sum / temps.size();
```

# while
```cpp
// exp가 true인동안
while (exp):
    statement
```


# do while
```cpp
int selection {};
do
{
    double width{}, height{};
    cout << "enter width and height separated by a space :" ;
    cin >> width >> height;

    double area {width * height};
    cout << "The area is" << area << endl;

    cout << "Calculate another (Y/N) : ";
    cin >> selection;
}while (selection == Y || selection == 'y');
{
    cout << "Thanks!" << endl;
}
```

# 2중 for statement
```cpp
int gird[5][3] {};
for (row = 0; row < 5; ++i){
    for (int col {0}; col < 3; ++col){
        gird[row][col] = 1000;
    }
}
```

```cpp
vector<vector<iut>> vector_2d
{
    {1,2,3},
    {10,20,30,40},
    {100,200,300,400,500}
};
for (auto vec:vector_2d){
    for (auto num:vec){
        cout << num << endl;
    }
    couy << endl;
}
```

```cpp
#include <vector>
#include <iostream>
using namespace std;
int main()
{
    vector<int> data {};
    for(int i {1}; i <= num_items; ++i){
        int num_items {};
        cout << "Enter data item" << i << ":";
        cin >> num_items;
        data.push_back(num_items);      
    }

    cout << "\nDisplaying Histohram" << endl;
    for (auto val : data){
        for (int i{1}; i <= val; ++i)
        {
            if (i%5 == 0)
                cout << "*";
            else
                cout << "-";                
        }
        cout << endl;
    }
    cout << endl;
    return 0;  
}
```