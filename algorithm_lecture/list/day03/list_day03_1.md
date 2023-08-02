# 2차원 배열


## 순회방법
1. 행 우선 순회
```python
for i in range(n):
    for j in range(m)
        function(Array[i][j])
```
2. 열 우선 순회
```python
# 행은 그대로 두고 열먼저 돌고 행출력
for j in range(m)
    for i in range(n):
        function(Array[i][j])
```
3. 지그재그 순회
```python
for i in range(n):
    for j in range(m)
        # 짝수 홀수를 지우거나 남길때 사용
        function(Array[i][j + (m - 1 - 2 * j) * (i%2)])
```

### 델타를 이용한 탐색
```python
arr[][] # nxn배열
# 원소 i를 기준으로 상하좌우를 탐색
# di, dj를 바꿈으로써 탐색 범위를 조절가능
di[0, 1, 0, -1] #행에대한 방향
dj[1, 0, -1, 0] #열에대한 탐색
for i in range(len(arr))
    for j in range(len(arr))
        for k in range(4): # 4방향에 대해서
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= ni < N: # 인덱스검사
                f(arr[ni][nj]) 
```

### 전치 행렬
```python
# 대각행렬을 기준으로 값들을 변경
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        # 대각 행렬의 오른쪽 위 요소들을 바꿀것
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```
