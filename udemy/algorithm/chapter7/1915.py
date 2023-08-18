# N x M 배열
# 가장 큰 1로 이루어진 정사각형을 판별

N, M = map(int, input().split())

arr = [input() for _ in range(N)]
dp = [[0] * M for _ in range(N)]
# 결국 dp 문제 dp 의 좌표에 좌상단 위 왼쪽 의 값을 비교해서 최대 크기를 판별
for j in range(M):
    if arr[0][j] == '1':
        dp[0][j] == '1'


for i in range(1,N):
    if arr[i][0] == '1':
        dp[i][0] == 1
    for j in range(M):
        if arr[i][j] == '1':
            dp[i][j] == min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) +1

ans = 0
for i in range(N):
    ans = max(ans, dp[i])

print(ans**2)