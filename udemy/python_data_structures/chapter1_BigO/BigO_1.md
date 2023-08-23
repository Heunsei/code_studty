# BigO
- 코드가 얼마나 효율적으로 돌아가는지 측정하는것
- time complexity 시간복잡도
- space complexity 공간복잡도
- 최악의 경우와 최선의 경우를 비교해서 측정


# 표현방법
- 오메가 Ω     > best case
- 세타 Θ      > average case
- 오미크론 O    > worst case
- 대부분 시간복잡도를 말할때 최악의 경우를 계산

### O(n)
- n개 만큼의 연산을 실행
```python
def print_items(n):
    for i in range(n):
        print(i)
```
```python
- N + N 이라 O(2N)이지만 2는 생략하고 O(N)으로 표현
def print_items(n):
    for i in range(n):
    print(i)
    for j in range(n):
    print(j)
```
- N * N > O(N^2)
```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
```
- O(n^2) + O(n) > 밑에있는 n은 날림
```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
```
- 분할 정복이 대부분 O(logN)
  
- 유용한 사이트, 데이터 구조별로 시간복잡도 / 공간복잡도 알려줌
- https://www.bigocheatsheet.com/