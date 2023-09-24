import heapq

def dijkstra():
    dist = [E * 100] * (V+1)
    q = []
    heapq.heappush(q, (0,0))
    dist[0] = 0

    while q:
        W, node = heapq.heappop(q)
        if dist[node] < W:
            continue
        
        # 인접 노드 모두 조회
    for next in range(len(arr[node])):
        # 갈수 있는지 판별
        if arr[node][next] != E*100:
            next_node = next
            cost = arr[node][next]

            new_cost = cost + W
            if dist[next] <= next_node:
                continue
            dist[next_node] = new_cost
            heapq.heappush(q, (new_cost, next_node))
    return dist

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[E*100] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        S, E, W = map(int,input().split())
        arr[S][E] = W
