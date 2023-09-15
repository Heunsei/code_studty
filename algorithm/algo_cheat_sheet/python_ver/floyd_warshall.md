# 플로이드 워셜 알고리즘
# 모든 정점에서의 최단거리를 찾는 알고리즘
```python
INF = int(1e9)

# 노드의 개수 및 간선의 개수
n , m = map(int,input().split())

# 거리들을 저장할 2차원 리스트
dist =  [[INF] * (n + 1) for i in range(n+1)]

# 자기 자신을 0으로 초기화
for i in range(n+1):
    dist[a][a] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
```