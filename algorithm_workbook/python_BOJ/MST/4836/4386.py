import math
import heapq
import sys
#sys.stdin = open('input.txt')
# N개의 별들을 이어서 별자리 를 만듬
# 별자리 를 이루는 선은 서로 다른 두 별을 일직선 으로 이은 형태
# 모든 별들은 별자리 위의 선을 통해 서로 직/간접 적으로 이어져 있어야 함
# 선을 하나 이을 때 마다 두 별 사이의 거리 만큼 의 비용이 들때 별자리 를 만드는 최소 비용


def prim(start):
    hq = []
    mst = [0] * N
    heapq.heappush(hq, (0, start))
    sum_weight = 0
    while hq:
        weight, current = heapq.heappop(hq)
        if mst[current]:
            continue
        mst[current] = 1
        sum_weight += weight
        for next in range(N):
            if mst[next] or node[current][next] == 0:
                continue
            heapq.heappush(hq,(node[current][next], next))
    return sum_weight

N = int(input())
graph = [list(map(float, input().split())) for _ in range(N)]
node = [[0]*(N) for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        x1, y1 = graph[i][0], graph[i][1]
        x2, y2 = graph[j][0], graph[j][1]
        dist = math.sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)
        # node[i].append((j, dist))
        # node[j].append((i, dist))
        node[i][j] = dist
        node[j][i] = dist

res = prim(0)
print(f'{res:.2f}')
