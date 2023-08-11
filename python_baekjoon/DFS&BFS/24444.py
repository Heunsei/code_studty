# BFS 구현문제
from collections import deque
import sys
input = sys.stdin.readline
# 정점의 수, 간선의 개수, 시작 정점
N, M, R = map(int, input().split())
board = [[] for _ in range(N + 1)]
visited = [0] * (N+1)
# 보드에 값 넣어두기
cnt = 1
def BFS(start):
    global cnt
    visited[start] = cnt
    dq = deque()
    # 시작값 삽입
    dq.append(start)
    while dq:
        now = dq.popleft()
        for i in board[now]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                dq.append(i)

for _ in range(M):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

for i in range(N+1):
    board[i].sort()
    board[i].reverse()

BFS(R)
for i in range(1, N+1):
    print(visited[i])
