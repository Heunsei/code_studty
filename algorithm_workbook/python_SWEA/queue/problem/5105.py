from collections import deque
T = int(input())

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

def isInRange(i, j):
    return 0 <= i < N and 0 <= j < N

def bfs(pos_i, pos_j):
    visited = [[False] * N for _ in range(N)]
    dq = deque()
    # dq 에 넣어줄 때 count를 저장할 0을 같이 넣어줌
    dq.append((pos_i, pos_j, 0))
    visited[pos_i][pos_j] = True
    while dq:
        # 좌표 1,2 count
        i, j, d = dq.popleft()
        # 도착점을 만나면 d를 출력
        if arr[i][j] == '3':
            return d - 1
        nd = d + 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if isInRange(ni, nj) and not visited[ni][nj] and arr[ni][nj] != '1':
                visited[ni][nj] = True
                dq.append((ni, nj, nd))
    return 0

for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                pos_i = i
                pos_j = j

    res = bfs(pos_i, pos_j)
    print(f'#{tc} {res}')
