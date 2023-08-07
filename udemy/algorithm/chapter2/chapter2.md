### 완전탐색
- 장점 : 반드시 답을 찾을 수 있다
- 단점 : 오래걸림, 리소스 많이잡아 먹음
- 얼마나 오래걸릴지 시간안에 돌아가는지 확인이 필요

### 브루트 포스
- 무자별 대입법
- 전부다 때려박기, 언젠가는 맞는다
- 가장 확실한 방법이라 생각보다 많이씀

### n개의 수를 받아서 두 수를 뽑아 합이 가장 클때
- 이중포문 돌릴텐데 O(N^2)......수가 크다면...
- 정렬해서...맨뒤값만 더해볼까..?
- sort는 O(NlogN) 나오니까 이거라면...?

### 순열
- 모든 경우의 수를 살펴볼때 용이
- permutation 또는 next_permutation
- cpp는 벡터를 정렬해서 반복문을 써야함 주로 do while을 씀
```cpp
import algorithm

vector<int> v{0,1,2,3};
do{
    for(int i : v) printf(" %d", i);
    
    printf("\n")
}while (next_perutation(v.begin(), v.end()));
```

```python
from itertools import permutations
v = [0,1,2,3]
# v 배열의 이름, v 몇개뽑을지(순열이 원소 몇개로 이루어져 있는지)
for i in permutations(v,4):
    print(i)
```

### 조합
- 파이썬은 combination 기본제공
```python
from itertools import combinations
v = [0, 1, 2, 3]

for i in combinations(v,2):
    print(i)
    
```