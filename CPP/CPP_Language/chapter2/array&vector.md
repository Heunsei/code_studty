# 배열과 백터

## Array(배열)
- 고정된 크기
- 모든 요소들이 같은 데이터 타입을 가짐
- itreation 가능
- no bound check

```cpp
int test_scores[5];
int high_score_per_level [10] {3,5} // 나머지 0으로
int another_array [] {1,2,3,4,5}; // 크기 자동으로 계산
```
## 배열에 접근
```cpp
int test_score [5] {100, 95, 99, 87, 88};

cin >> test_score[0];
cin >> test_score[1];
cin >> test_score[2];
cin >> test_score[3];
cin >> test_score[4];
```
- 접근 2
```cpp
# include <iostream>
using namespace std;
int main(){
    char vowels[] {a,e,i,o,u};
    cout << "\nThe First vowel is:" << vowels[0] << endl;
    cout << "\nThe Last vowel is:" << vowels[4] << endl;

    int test_scores[5] = {100, 90};
}
```

# Vector - 벡터
- STL 컨테이너
- 동적배열
- sort, reverse, find 같은 함수 사용가능
- type이 모두 같아야 함

- 선언방법
```cpp

# include <vector>
using namespace std;
// vector<val_type> vetcor_name;
vector <int> test_score;
// 접근할때 []를 사용해 바로 접근이 가능하지만 at(1) 이런식으로도 접근 가능
```

- vector
```cpp
# include <vector>
# include <iostream>

using namespace std;
int main(){
    // vector <char> vowels; // empty
    // vector <char> vowels (5); // 5 init to zero
    // vector <char> vowels (5, 100); // 5 init to 100

    vector <char> vowels {'a', 'e', 'i', 'o', 'u'};
    
    cout << vowels[0] << endl;
    cout << vowels[4] << endl;

    int score_to_add {0};
    cin >> score_to_add;
    test_score.push_back(score_to_add)
}
```