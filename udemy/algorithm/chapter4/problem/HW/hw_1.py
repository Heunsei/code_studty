from collections import deque

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

def is_validate(position1, position2):
    return 0 <= position1 < 16 and 0 <= position2 < 16


def BFS(i, j):
    visited = [[False] * 16 for _ in range(16)]
    dq = deque()
    dq.append((i,j))
    visited[i][j] = True
    while dq:
        str_i, str_j = dq.pop()
        if graph[str_i][str_j] == '3':
            return 1
        for k in range(4):
            ni = str_i + di[k]
            nj = str_j + dj[k]
            if is_validate(ni, nj) and not visited[ni][nj] and graph[ni][nj] != '1':
                visited[ni][nj] = True
                dq.append((ni, nj))
    return 0

for _ in range(10):
    tc = int(input())

    graph = [list(input()) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if graph[i][j] == '2':
                start_i = i
                start_j = j

    ans = BFS(start_i,start_j)
    print(f'#{tc} {ans}')
