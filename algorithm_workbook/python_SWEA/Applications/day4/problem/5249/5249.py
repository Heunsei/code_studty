# 최소 신장 트리를 만드는 것
import heapq
def prim(start):
    hq = []
    # 노드의 개수만큼 방문체크 배열 생성
    visited = [0] * (V+1)
    # 가중치랑 시작 노드 번호를 제공
    heapq.heappush(hq, (0, start))
    acc = 0

    while hq:
        weight, v = heapq.heappop(hq)
        if visited[v]:
            continue
        visited[v] = 1
        acc += weight
        for next in graph[v]:
            next_node = next[0]
            next_weight = next[1]
            if visited[next_node]:
                continue
            heapq.heappush(hq, (next_weight, next_node))
    return acc


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[]  for _ in range(V+1)]
    for _ in range(E):
        start, end, w = map(int, input().split())
        graph[start].append((end, w))
        graph[end].append((start,w))
    res = prim(0)
    print(f'#{tc} {res}')