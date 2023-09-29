# MST 를 구하는 prim 알고리즘
# 정점 / 간선
# 정점에 비해 간선이 적은 희소 그래프 에서는 크루스칼 알고리즘 이 적합
# 정점에 비해 간선이 많은 밀집 그래프 에서는 프림 알고리즘 이 적합

import heapq


def prim(start):
    heap = []
    # MST 에 방문 했는지 안했는지를 관리해야함
    MST = [0] * V
    # 가중치 와 정점 정보 를 heap 에 저장
    heapq.heappush(heap, (0, start))
    sum_weight = 0
    while heap:
        print(heap)
        # 우선순위가 높은것을 꺼냄
        # v는 방문 지점
        weight, v = heapq.heappop(heap)
        if MST[v]:
            continue
        # 방문 체크
        MST[v] = 1
        # 누적값
        # 방문시점이 최단거리라 이걸 뺄 일이 없음
        sum_weight += weight
        for next in graph[v]:
            if graph[v][next] == 0 or MST[next]:
                continue
            heapq.heappush(heap, (graph[v][next], next))
    return sum_weight


V, E = map(int, input().split())
graph =[[0] * V for _ in range(V)]

for _ in range(E):
    # 그래프에 담겨있는것은 가중치
    f, t, w = map(int,input().split())
    graph[f][t] = w
    graph[t][f] = w
print(prim(0))
