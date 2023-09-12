import sys
from collections import deque
#sys.stdin = open('input.txt')

def bfs():
    dq = deque()
    dq.append((home[0], home[1]))
    while dq:
        x, y = dq.popleft()
        if abs(x-fest[0]) + abs(y-fest[1]) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nxt_x, nxt_y = gs25[i][0], gs25[i][1]
                if abs(x - nxt_x) + abs(y - nxt_y) <= 1000:
                    visited[i] = True
                    dq.append((nxt_x,nxt_y))
    print('sad')
    return



T = int(input())
for _ in range(T):
    n = int(input())
    home = list(map(int, input().split()))
    gs25 = [list(map(int,input().split())) for _ in range(n)]
    fest = list(map(int, input().split()))
    visited = [False] * (n + 1)
    bfs()