# 부분 수열의 합
# i >> 깊이, N >> 수열의 길이, s >> 지금까지의 누적합, K >> 찾아야 하는 합
def f(i, N, s, K):
    global cnt
    if i == N:
        if s == K:
            cnt += 1
    # 가지 치기
    elif s > K:
        return
    else:
        f(i+1, N, s+arr[i], K)
        f(i+1, N, s, K)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
