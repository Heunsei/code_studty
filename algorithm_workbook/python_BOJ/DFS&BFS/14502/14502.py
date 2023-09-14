from collections import deque
import copy
import sys
input = sys.stdin.readline


def is_valid(ni, nj):
    return 0 <= ni < N and 0 <= nj < M

def bfs():
    global ans
    dq = deque()
    test = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if test[i][j] == 2:
                dq.append((i,j))
    while dq:
        pos_i, pos_j = dq.popleft()
        for k in range(4):
            ni = pos_i + di[k]
            nj = pos_j + dj[k]
            if is_valid(ni,nj) and test[ni][nj] == 0:
                test[ni][nj] = 2
                dq.append((ni,nj))
    tmp = 0
    for i in range(N):
        for j in range(M):
            if test[i][j] == 0:
                tmp += 1
    ans = max(ans, tmp)

def make_wall(count):
    if count == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    make_wall(count+1)
                    arr[i][j] = 0


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
make_wall(0)
print(ans)