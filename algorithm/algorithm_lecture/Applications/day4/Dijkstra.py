import heapq
# 다익스트라 알고리즘
def dijkstra(start):
    pq = []
    # 출발점초기화 dist 는 0
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 방문한 지점일때 누적 거리가 더 짧으면 pass
        # 돌아 돌아 방문지점에 도착 할 수도 있음
        if distance[now] < dist:
            continue
        # 인접 노드 확인
        for nxt in graph[now]:
            nxt_node = nxt[0]
            cost = nxt[1]
             
            # 다음 노드로 가기위한 누적 거리
            nxt_cost = dist + cost
            
            # 누적거리가 기존보다 크다면
            if distance[nxt_node] < nxt_cost:
                continue

            distance[nxt_node] = nxt_cost
            heapq.heappush(pq,(nxt_cost,  nxt_node))
        
        

# 누적 거리를 저장
# 우선순위 큐를 사용
n,m = map(int, input().split())
graph = [[] for _ in range(n)]
INF = int(1e9) # 대충 짱 큰 수
distance = [INF] * n
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t,w])


