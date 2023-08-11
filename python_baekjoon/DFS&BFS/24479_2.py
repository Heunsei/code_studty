import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 정점의수, 간선의 수 , 시작값
N, M, R = map(int, input().split())
# 간선표시
adj = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
count = 1

def DFS(start):
    global count
    # 방문 표시 및 카운트
    visited[start] = count
    adj[start].sort()
    adj[start].reverse()
    for t in adj[start]:
        if visited[t] == 0:
            count += 1
            DFS(t)

# 간선정보 입력
# 무방향 리스트
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

DFS(R)
for i in range(1, N+1):
    print(visited[i])