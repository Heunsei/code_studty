# 정점의 갯수
N = 7
# 간선의 갯수
M = 8
adj = [[0]*N for _ in range(M)]
# 0 1 2 3 4 5 6 7
chk = [False] * N
result = 0

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            print(nxt)
            dfs(nxt)

for i in range(M):
    a, b = map(int, input().split())
    adj[a-1][b-1] = adj[b-1][a-1] = 1

for i in range(N):
    if not chk[i]:
        result += 1
        chk[i] = True
        dfs(i)