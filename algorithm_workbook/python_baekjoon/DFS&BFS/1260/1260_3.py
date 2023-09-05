N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def bfs(start):
    visited = [False] * (N+1)
    visited[start] = True
    stk = [start]
    while stk:
        idx = stk.pop(0)
        print(idx, end=' ')
        for nxt in graph[idx]:
            if not visited[nxt]:
                visited[nxt] = True
                stk.append(nxt)


dfs_check = [False] * (N+1)
def dfs(start):
    dfs_check[start] = True
    print(start, end=' ')
    for nxt in graph[start]:
        if not dfs_check[nxt]:
            dfs_check[nxt] = True
            dfs(nxt)


dfs(V)
print()
bfs(V)