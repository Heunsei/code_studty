# V개의 노드와 E개의 간선정보
from collections import deque
T = int(input())

def bfs(start, end):
    visited = [0] * (V+1)
    dq = deque()
    dq.append(start)
    visited[start] = 1
    while dq:
        now = dq.popleft()
        if now == end:
            return visited[now]
        for nxt in adj[now]:
            if visited[nxt] == 0:
                dq.append(nxt)
                visited[nxt] = visited[now] + 1
    return 1

for tc in range(1, 1+T):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    start, end = map(int, input().split())

    res = bfs(start, end)-1
    print(f'#{tc} {res}')