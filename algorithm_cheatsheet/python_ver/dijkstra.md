# 하나의 시작 정점으로 부터 모든 다른 정점까지의 최단 경로를 찾는 알고리즘
```python
import heap
INF = int(1e9)

# 노드의 개수 간선의 개수
n, m = map(int,input().split)
# 시작노드
start = int(input())
# 각 노드에 연결된 리스트
graph = [[] for i in range(n+1)]
# 최단거리를 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단경로는 0으로 설정하여 큐에 삽입하는 과정
    # 거리값 , 시작좌표
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heaq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
```