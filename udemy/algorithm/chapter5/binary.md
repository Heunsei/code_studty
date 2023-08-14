# lower / upper_bound
# 
```cpp
// 여기서 end는 [ ) 반열림구간 end-1 이란 뜻
// 탐색범위를 제공하고 3을 찾는것
// 찾는 값을 포함해서 같거나 큰값중에 처음으로 나오는 곳의 위치를 반환
// lower_bound 찾으려는 key값보다 같거나 큰 숫자가 배열에 몇 번째에서 처음 등장 하는지를 찾기위함
// upper_bound 찾으려는 key값을 초과하는 숫자가 배열의 몇 번째에 등장하는지 찾기위함
#include<algorithm>
vector<int> v = {0, 1, 3, 3, 6, 6, 6, 7, 8, 8}
int three = upper_bound(v.begin(), v.end(), 3) - lower_bound(v.begin(), v.end(), 3)
printf("number of 3: %dn", three);
```

```python
from bisect import bisect_left, bisect_right
v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
# 3을 초과하는 첫 값의 idx - 3을 포함하는 첫 값의 idx
three = bisect_right(v, 3) - bisect_left(v, 3)
```

# 파라매트릭 서치
- 최적화 문제
  1. 기준선 보다 높고 낮은걸 찾아서 최소 최대를 찾기?
  2. 선형 탐색으로 하면 O(N)만큼 시간이 걸리니까 너무 오래걸림
  3. 어떤 기준이후로는 값이 보장되어 있기 때문에 뒤는 탐색을 안해도 됨   
- yes or no 찾기

- 매개변수 parameter 가 주어지면 ture or false 가 결정 되어야함
- 가능한 해의 범위가 연속적이어야함
- 범위를 반씩 줄이며 true false 를 구한다
- 이진탐색과 똑같음
- 경계선을 찾는듯한 느낌이 강함
