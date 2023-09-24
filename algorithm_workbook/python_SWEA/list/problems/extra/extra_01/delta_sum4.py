T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0
    for i in range(N):
        for j in range(M):
            tmp = arr[i][j]
            for k in range(4):
                for m in range(1, arr[i][j] + 1):
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < M:
                        tmp += arr[ni][nj]
            if tmp > max_val:
                max_val = tmp
    print(f'#{tc} {max_val}')