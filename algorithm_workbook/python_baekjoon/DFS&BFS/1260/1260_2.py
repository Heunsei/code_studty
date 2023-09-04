from collections import deque
N, M, V = map(int, input().split())

adj = [[] for _ in range(N+1)]
chk_bfs = [False] * (N+1)
chk_dfs = [False] * (N+1)


for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in adj:
    i.sort()

def bfs(start):
    chk_bfs[start] = True
    dq = deque([start])
    while dq:
        nxt = dq.popleft()
        print(nxt, end=' ')
        for i in adj[nxt]:
            if not chk_bfs[i]:
                dq.append(i)
                chk_bfs[i] = True

def dfs(start):
    chk_dfs[start] = True
    print(start, end=' ')
    for nxt in adj[start]:
        if not chk_dfs[nxt]:
            dfs(nxt)


dfs(V)
print()
bfs(V)
