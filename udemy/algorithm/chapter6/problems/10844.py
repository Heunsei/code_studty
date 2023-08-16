MOD = 1_000_000_000

cache = [[0] * 10 for _ in range(101)]
for j in range(1, 10):
    # 길이가 1일때 1~9 는 한개의 뒷 숫자를 가짐
    cache[1][j] = 1

# 길이가 N인 계단수의 숫자를 계산하는 문제

for i in range(2, 101):
    for j in range(10):
        if j > 0:
            # 0 일때는 아래 조건문때문에 하나만 들어가짐
            cache[i][j] += cache[i-1][j-1]
            cache[i][j] %= MOD

        if j < 9:
            # 9일때는 8만 들어갈 수 있으니까 윗 조건문에 의해 하나만
            cache[i][j] += cache[i-1][j+1]
            cache[i][j] %= MOD

ans = 0
N = int(input())
for j in range(10):
    ans += cache[N][j]
    ans %= MOD

print(ans)