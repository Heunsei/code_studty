# 칸채우기
MOD = 10007
dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD

T = int(input())

print(dp[T])

