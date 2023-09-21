import heapq
def dijkstra():
    dist = [E * 100] * (V+1)
    visited = [0] * (V+1)
    # 시작지점은 항상 가중치가 0이어야함
    dist[0] = 0
    for _ in range(V):
        next = 0
        min_val = E * 100

        for i in range(V+1):
            if not visited[i] and min_val > dist[i]:
                next = i
                min_val = dist[i]
        visited[next] = 1
        print(dist)
         # 모든 노드에 대해서 도착할 수 있는 최소 가중치 갱신
        for j in range(V+1):
            if not visited[j] and dist[j] > dist[next] + arr[next][j]:
                dist[j] = dist[next] + arr[next][j]
    return dist[V]


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    arr = [[E*100] * (V+1) for _ in range(V+1)]
    INF = int(1e9)

    for i in range(E):
        S, E, W = map(int, input().split())
        arr[S].append([E,W])
    print(dijkstra())