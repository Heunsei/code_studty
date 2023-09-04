# DFS로 탐색한결과 and BFS로 탐색한 결과 출력
from collections import deque


def dfs(start):
    visited_dfs[start] = True
    print(start, end=' ')
    for i in adj[start]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(start):
    dq = deque([start])
    visited_bfs[start] = start
    while dq:
        V = dq.popleft()
        print(V, end=' ')
        for i in adj[V]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                dq.append(i)


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)


for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in adj:
    i.sort()

dfs(V)
print()
bfs(V)
