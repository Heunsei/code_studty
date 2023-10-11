import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
graph = [[] for _ in range(N+1)]


def dfs(start, weight):
    for i in graph[start]:
        a, b = i
        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a, weight + b)


for _ in range(N-1):
    # 부모노드, 자식노드, 가중치
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번부터 각 노드까지의 거리를 -1로 설정
distance = [-1] * (N+1)
distance[1] = 0
# 시작 부모노드는 항상 1이라 조건
dfs(1, 0)

# 가장 멀리있는것부터 다시 dfs 를 돌리면됨
start = distance.index(max(distance))
distance = [-1] * (N+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))