# 사실 풍선문제
T = int(input())
for tc in range(1, 1+T):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for k in range(4):
                for m in range(1, arr[i][j]+1):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]
            if max < cnt:
                max = cnt
    print(max)



