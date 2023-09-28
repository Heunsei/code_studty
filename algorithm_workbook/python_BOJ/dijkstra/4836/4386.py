import math
import heapq
import sys
sys.stdin = open('input.txt')
# N개의 별들을 이어서 별자리 를 만듬
# 별자리 를 이루는 선은 서로 다른 두 별을 일직선 으로 이은 형태
# 모든 별들은 별자리 위의 선을 통해 서로 직/간접 적으로 이어져 있어야 함
# 선을 하나 이을 때 마다 두 별 사이의 거리 만큼 의 비용이 들때 별자리 를 만드는 최소 비용


def dijk(start):
    hq = []
    # 현재 좌표까지의 거리는 0이므로 거리와 현재 좌표값을 넣어줌
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        d, current = heapq.heappop(hq)
        if distance[int(current)] < d:
            continue
        for next in node[int(current)]:
            next_node = next[0]
            cost = next[1]
            next_cost = cost + d
            if distance[next_node] < next_cost:
                continue
            distance[next_node] = next_cost
            heapq.heappush(hq, (next_cost, next_node))


N = int(input())
graph = [list(map(float, input().split())) for _ in range(N)]
node = [[] for _ in range(N)]
INF = 987654321
distance = [INF] * N
res = 987654321
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = graph[i][0], graph[i][1]
        x2, y2 = graph[j][0], graph[j][1]
        dist = math.sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)
        node[i].append((j, dist))
        node[j].append((i, dist))

for i in range(N):
    dijk(i)
    print(distance)
    tmp = 0
    for j in distance:
        tmp += j
    res = min(res, tmp)
    for k in range(N):
        distance[k] = INF

print(round(res,2))
