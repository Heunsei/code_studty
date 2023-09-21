# E개의 일방통행 도로구간
# 연결 지점에는 0번부터 N번까지의 번호가 붙어있다
# 0번부터 N번까지 가는데 최소한의 거리가 얼만지 찾기
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 인접한 다른 노드 확인 i 에는 (다음노드, 가중치가 들어있음)
        for i in graph[now]:
            cost = dist + i[1]
            # 이동거리가 더 짧다면
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    for _ in range(E):
        start, end, dist = map(int, input().split())
        graph[start].append((end,dist))
    dijkstra(0)
    res = distance[N]
    print(f'#{tc} {res}')
