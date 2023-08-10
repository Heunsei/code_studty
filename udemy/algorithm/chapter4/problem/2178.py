# 미로찾기
# i, j의 크기
from collections import deque

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)
N, M = map(int, input().split())
# 붙어서 주어지기 때문에 string
board = [input() for _ in range(N)]

def is_valid_coord(i, j):
    return 0 <= i < N and 0 <= j < M

def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    # BFS 는 덱으로 구현
    dq = deque()
    dq.append((0, 0, 1))  # 탐색 시작값의 좌표 세번쨰는 count
    while dq:
        i, j, d = dq.popleft()  # 덱에서 좌표하나를 뽑아와서 사용
        if i == N-1 and j == M-1:
            return d

        nd = d + 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if is_valid_coord(ni, nj) and board[ni][nj] == '1' and not chk[ni][nj]:
                chk[ni][nj] == True
                dq.append((ni, nj, nd))

print(bfs())