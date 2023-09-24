# 1번부터 N번까지 도시 M개의 단방향 노드
# X번 도시에 K 거리만큼 걸리는 도시의 번호를
import heapq
def dijk(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            next_cost = dist + cost
            if distance[next_node] < next_cost:
                continue
            distance[next_node] = next_cost
            heapq.heappush(hq,(next_cost, next_node))


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

dijk(X)
#print(distance)
if K not in distance:
    print('-1')
else:
    for i in range(1,N+1):
        if distance[i] == K:
            print(i)
