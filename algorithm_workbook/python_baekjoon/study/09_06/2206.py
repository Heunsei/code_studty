# 벽뿌셔 다뿌셔
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
can_break = True
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < M


def dfs(start, possibility):
    start_i, start_j, move_count = start
    if start_i == N-1 and start_j == M-1:
        return move_count
    for k in range(4):
        ni = start_i + di[k]
        nj = start_j + dj[k]
        if is_valid(ni, nj) and arr[ni][nj] == 1 and not visited[ni][nj] and possibility:
            visited[ni][nj] = True
            possibility = False
            arr[ni][nj] = 0
            dfs((ni, nj, move_count+1), possibility)
            possibility = True
            arr[ni][nj] = 1
        elif is_valid(ni, nj) and arr[ni][nj] == 0 and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs((ni, nj, move_count+1), possibility)


res = dfs((0, 0, 0), can_break)
print(res)
