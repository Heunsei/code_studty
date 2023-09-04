T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def isvalidate(i,j):
    return 0 <= i < N and 0 <= j < M

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            val = arr[i][j]
            for k in range(4):
                for m in range(1, arr[i][j]+1):
                    ni = i + (di[k] * m)
                    nj = j + (dj[k] * m)
                    if isvalidate(ni, nj):
                        val += arr[ni][nj]
            if result < val:
                result = val

    print(f'#{tc} {result}')
