from collections import deque
import sys
input = sys.stdin.readline
#sys.stdin = open('input.txt')
# 단지 번호 붙이기
cnt = 0

def is_valid(ni, nj):
    return 0 <= ni < N and 0 <= nj < N


def color(i, j):
    dq = deque([(i, j)])
    visited[i][j] = True
    house[i][j] = -1
    tmp = 0
    while dq:
        nxt_i, nxt_j = dq.popleft()
        tmp += 1
        for k in range(4):
            ni = nxt_i + di[k]
            nj = nxt_j + dj[k]
            if is_valid(ni, nj) and not visited[ni][nj] and house[ni][nj] == '1':
                visited[ni][nj] = True
                house[ni][nj] = -1
                dq.append((ni, nj))
    res.append(tmp)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
house = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
res = []

for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        visited[i][j] = True
        if house[i][j] == '1':
            color(i, j)
            cnt += 1
res.sort()
print(cnt)
for i in res:
    print(i)
