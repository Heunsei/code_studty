# 스택
- 스택의 특성
- 결국은 리스트로씀
1. 물건을 쌓아 올리듯 자료를 쌓아올린 자료구조
2. 선형구조
3. **후입선출(LIFO)** 
4. 마지막 원소가 top 이라 불림
- 연산
1. 삽입 > push
2. 삭제 > pop
3. isEmpty
4. peek

# 재귀 함수
```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

```python
N = 30
memo = [0] * (N+1)
def fibo(n):
    global cnt
    global  memo
    
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibo(n-1) + fibo(n-2)
        return memo
```

```python
# 작은수들을 저장해서 (글로벌로) 반복문에서 쓸때 이미 만든값이면 그걸 꺼내와서 사용
# 메모이제이션 > 넣어왔다가 필요한값만 꺼내쓰는것0
def fibo2(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
f = [0] * 100
print(fibo2(100))
```
```python
# 방문을 표시할 배열
visited = [False] * N
stack = []
def dfs(num):
```

### DFS
- 비선형 구조에서 모든 자료를 빠짐없이 검색하는것이 중요함
- 정점을 연결되어있는 간선을 이차원 배열로 만들어서 연결을 표현
- 이중리스트를 전부 탐색할것 0번째줄 중에 j의 값이 있다~없다

```python

```