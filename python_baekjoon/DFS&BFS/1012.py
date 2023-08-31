di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < M


def search(i, j):
    global count
    count += 1
    stack = []
    stack.append((i, j))
    while stack:
        pos_i, pos_j = stack.pop()
        for k in range(4):
            ni = pos_i + di[k]
            nj = pos_j + dj[k]
            if is_valid(ni, nj) and arr[ni][nj] == 1:
                stack.append((ni, nj))
                arr[ni][nj] = 0


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    count = 0
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                search(i, j)
    print(count)


