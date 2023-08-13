import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, M, R = map(int, input().split())
adj = [[] for _ in range(N+1)]
# 방문여부와 순서를 저장
visited = [0] * (N+1)
# global로 전역변수를 관리
cnt = 1

def DFS(t):
    global cnt
    # 첫 방문값은 1
    # 이중배열로 정점의 연결을 표시
    visited[t] = cnt
    adj[t].sort()
    for i in adj[t]:
        if visited[i] == 0:
            cnt += 1
            DFS(i)


for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

DFS(R)

for i in range(1, N + 1):
    print(visited[i])