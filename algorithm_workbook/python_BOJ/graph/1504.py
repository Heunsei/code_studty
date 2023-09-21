import heapq
def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0, start))
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]
            if distance[next_node] < dist + cost:
                continue
            next_cost = dist + cost
            distance[next_node] = next_cost
            heapq.heappush(hq,(next_cost, next_node))


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)
for _ in range(E):
    start, end, dist = map(int,input().split())
    graph[start].append((end,dist))
    graph[end].append((start,dist))
v1, v2 = map(int,input().split())

dijkstra(v1)
to_v1 = distance[1]
v1_to_v2 = distance[v2]
v1_to_end = distance[N]
distance = [INF] * (N+1)
dijkstra(v2)
to_v2 = distance[1]
v2_to_v1 = distance[v1]
v2_to_end = distance[N]

course1 = to_v1 + v1_to_v2 + v2_to_end
course2 = to_v2 + v2_to_v1 + v1_to_end
res = min(course2,course1)
if res >= INF:
    print('-1')
else:
    print(res)

