import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# DFS 구현
# 컴퓨터의 수 N < 100
N = int(input())
# 간선의 수
M = int(input())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

#1부터 시작
def DFS(start):
    global count
    visited[1] = True
    for k in adj[start]:
        if visited[k] == False:
            visited[k] = True
            count += 1
            DFS(k)

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

DFS(1)

print(count)