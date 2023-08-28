N = int(input())
arr = []
for i in range(1, N+1):
    arr.append(list(map(int, input().split())))
dp = [0] * (N+1)

for i in range(1, N+1):
    # 1일째 부터 확인
    # t는 전날의 소요 기간
    # p는 전날의 pay
    t, p = arr[i-1][0], arr[i-1][1]
    # 오늘 날짜 + 소요일이 퇴사일을 넘지 않으면
    if i + t - 1 <= N:
        dp[i+t-1] = max(dp[i+t-1], dp[i-1] + p)
    # 오늘이 어제보다 작다면
    # 최대값을 갱신
    if dp[i] < dp[i-1]:
        dp[i] = dp[i-1]
#print(arr)
print(max(dp))