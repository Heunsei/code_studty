# N - Queen
N = int(input())
arr = [[0] * N for _ in range(N)]
visited = [0] * N
# 0 > 왼쪽 위, 1 > 오른쪽 위
di = [-1, -1]
dj = [-1, 1]
cnt = 0

def is_valid(pos_i, pos_j):
    return 0 <= pos_i < N and 0 <= pos_j < N

def backtracking(depth, idx):
    global cnt

    if 1 in arr[depth]:
        return
    else:
        left_up_ni = depth + di[0]
        left_up_nj = idx + dj[0]
        right_up_ni = depth + di[1]
        right_up_nj = idx + dj[1]
        while left_up_ni < 0:



    for i in range(N):
        if visited[idx] == 1:
            continue
        visited[idx] = 1
        arr[depth][i] = 1
        backtracking(depth + 1, idx + 1)
        visited[idx] = 0
        arr[depth][i] = 0
