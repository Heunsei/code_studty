import heapq
def prim():
    Q = [(W, next) for next, W in G[0]]
    visited = [0] * (V+1)
    visited[0] = 1

    heapq.heapify(Q)
    acc = 0
    while Q:
        # 가장 작은 가중치를 먼저 순회
        W, now = heapq.heappop(Q)
        if not visited[now]:
            acc += W
            visited[now] = True
            for next, W in G[now]:
                if not visited[next]:
                    heapq.heappush(Q, (W, next))
    return acc

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    print(arr)
    G = [[] for _ in range(V+1)]

    for i in range(E):
        G[arr[i][0]].append([arr[i][1], arr[i][2]])
        G[arr[i][1]].append([arr[i][0], arr[i][2]])