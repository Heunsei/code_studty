# 연산 1 : A + 1
# 연산 2 : A * 2

A, K = map(int, input().split())
cnt = 0
while True:
    if A == K:
        print(cnt)
    if K % 2 == 0 and K >= A * 2:
        K //= 2
    else:
        K -= 1
    cnt += 1
print(cnt)