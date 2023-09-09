# 순열
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
```python
def dfs(depth, index):
    if depth == M:
        print(' '.join(map(str, pArr)))
        return
    for i in range(index, N+1):
        pArr.append(i)
        dfs(depth+1, i)
        pArr.pop()
dfs(0,1)
```
# 중복 순열 - 아직 미완
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

# 조합
```python
def comb(arr,n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in range(len(arr) - n + 1):
            for j in range(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result
```