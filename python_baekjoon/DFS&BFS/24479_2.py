N, M, R = map(int, input().split())
adj = [[0] * N for _ in range(N+1)]
visited = [0] * N
cnt = 1

def DFS(start):
   global cnt
   visited[start] = 1
   if star


for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1


