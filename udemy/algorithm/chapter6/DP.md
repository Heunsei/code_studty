### 동적 계획법
- 문제를 쪼개서 작은 무제의 답을 구하고, 그걸로 더 큰 문제의 답을 구하는것을 반복
- 분할정복과 비슷한 느낌

### top - down
- 재귀
- 메모이제이션
 1. 부분문제들의 답을 구하고 저장
 2. cache 에 저장해놓고 가져다 쓰자


### bottom - up
- 반복문
- 타뷸레이션
 1. 부분 문제들의 답을 미리 다 구해놓는것

### 피보나치 수열
```python
def fibo(N):
    f = [0] * (N+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, N + 1):
        f[i] = f[i-1] + f[i-2]
    return f[N]

```
### 이항계수 nCr
- 초기값과 점화식으로 구현
- bino(n,r) = bino(n-1,r-1) + bino(n-1,r)
- bino(n,0) = 1
- bino(n,n) = 1

```python
def bino(n, 0):
    pass
```
