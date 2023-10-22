# 순열
# visited 를 사용해 순서를 조절
```python
arr = [1, 2, 3, 4, 5]       # 후보를 찾을 배열
N = 3                   # 후보의 수
res = [0] * N       # result
check = [False] * len(arr)     # checker

def perm(depth):
    if depth == N:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(len(arr)):
            if check[i]:
                continue
            check[i] = True
            res[depth] = arr[i]
            perm(depth+1)
            check[i] = False
```

# 순열
- 아마 이게 맞지 싶다...?
```python
arr = [1,2,3,4,5]
N = len(arr)
visited = [False] * N
pArr = []
M = 2 # 우리가 구할 후보군의 길이

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, pArr)))
        return
    for i in range(N):
        if visited[i]:
            continue
        pArr.append(arr[i])
        visited[i] = True
        dfs(depth+1)
        pArr.pop()
        visited[i] = False
dfs(0)

```

# 조합
- 순서가 존재하지 않기 때문에 visited 를 사용하지 않음
```python
arr = ['a', 'b', 'c', 'd']  # 후보군들
n = len(arr)    # 주어진 후보들의 길이
r = 2           # 우리가 구할 조합의 길이
ans = []        # 답을 임시 저장할 배열

def combination(depth, idx):
    if depth == r:
        print(ans)
        return
    for nxt in range(idx, len(arr)):
        ans.append(arr[nxt])
        combination(depth + 1, nxt + 1)
        ans.pop()
```
5-3 = 2
```python
a= [3,6,7,1,5,4]
N = 6
for i in range(1<<N):
    subset1 = []
    for j in range(N):
            if i&(1<<j): # j번 비트가 0이 아니면
                subset1.append(a[j])
    print(*subset1)
```
```