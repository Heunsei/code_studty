# 순열을 만드는 코드
```python
def f(i, N):
    if i == N:  # 순열 완성
        print(p)
        return
    else:   # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:  # 아직 사용하지 않은 카드면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0

card = list(map(int, input()))
used = [0] * 6  # 이미 사용한 카드인지 표시
```
# 바이너리 카운팅
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
