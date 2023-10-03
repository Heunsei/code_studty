# 평범한 배낭
# 물품의 수, 버틸수 있는 무게
N, K = map(int,input().split())
arr = [0] * (K+1)
dp = [0] * (K+1)
for _ in range(N):
    a, b = map(int, input().split())
    arr[a] = b
    dp[a] = arr[a]

for i in range(1, K+1):
    tmp = [i for i in range(1,i+1)]

    dp[(2*i-1)] = max(arr[i] + arr[i-1] , dp[i])

print(arr)
print(dp)
print(max(dp))


