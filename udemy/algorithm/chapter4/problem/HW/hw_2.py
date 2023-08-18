di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def is_validate(pos_i, pos_j):
    return 0 <= pos_i < 16 and 0 <= pos_j < 16


def DFS(pos_i, pos_j):
    stack = []
    visited = [[False] * 16 for _ in range(16)]
    visited[pos_i][pos_j] = True
    stack.append((pos_i, pos_j))
    while stack:
        i, j = stack.pop()
        if graph[i][j] == '3':
            return 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if is_validate(ni, nj) and not visited[ni][nj] and graph[ni][nj] != '1':
                visited[ni][nj] = True
                stack.append((ni, nj))
    return 0
for _ in range(10):
    tc = int(input())
    graph = [list(input()) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if graph[i][j] == '2':
                start_i = i
                start_j = j

    ans = DFS(start_i, start_j)

    for i in graph:
        print(i)

    print(f'#{tc} {ans}')
