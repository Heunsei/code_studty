# N 개의 도시 M개의 버스
# A > B 까지가는데 최소비용
import heapq
import sys
input = sys.stdin.readline
def dijkstra(start):
    hq = []
    heapq.heappush(hq,[0, start])
    d[start] = 0
    while hq:
        dist, current = heapq.heappop(hq)
        if d[current] < dist:
            continue
        for next in graph[current]:
            next_node, cost = next[0], next[1]
            cost = dist + cost
            if d[next_node] > cost:
                d[next_node] = cost
                heapq.heappush(hq, [cost, next_node])



N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
d = [INF] * (N+1)
for i in range(M):
    a, b, dir = map(int, input().split())
    graph[a].append([b,dir])
start, end = map(int, input().split())
dijkstra(start)

print(d[end])