from collections import deque
from itertools import combinations as combi
import sys

INF  = 987654321
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(dq, blanks):
    visited = [[-1] * N for _ in range(N)]
    time = 0
    while True:
        length = len(dq)
        if blanks == 0 or length == 0:
            if blanks == 0:
                return time
            else:
                return INF
        time += 1
        for i in range(length):
            x, y = dq.popleft()
            if visited[x][y] == -1:
                visited[x][y] = 1

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    if visited[nx][ny] == -1:
                        if laboratory[nx][ny] == 0: # 빈칸
                            dq.append((nx,ny))
                            visited[nx][ny] = 1
                            blanks -= 1
                        elif laboratory[nx][ny] == 2: # 바이러스
                            dq.append((nx,ny))
                            visited[nx][ny] = 1


N, M = map(int ,input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]
virus = []
blank_cnt = 0
res = INF
for i in range(N):
    for j in range(N):
        if laboratory[i][j] == 0:
            blank_cnt += 1
        elif laboratory[i][j] == 2:
            virus.append((i,j))

for mem in combi(virus,M):
    dq = deque()
    for i in mem:
        dq.append(i)
    tmp = bfs(dq, blank_cnt)
    res = min(res, tmp)

if res == INF:
    print(-1)
else:
    print(res)