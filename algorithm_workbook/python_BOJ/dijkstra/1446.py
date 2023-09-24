# N개의 지름길 고속도로 길이 D
import heapq
def dijkstra(start,):
    h = []
    heapq.heappush(h, (0,start))
    distance[start] = 0
    while h:
        dist, cur = heapq.heappop(h)
        if distance[cur] < dist:
            continue
        # arr의 첫번쨰가 다음좌표, 가중치
        for next in arr[cur]:
            next_cost = dist + next[1]
            if distance[next[0]] < next_cost:
                continue
            distance[next[0]] = next_cost
            heapq.heappush(h, (next_cost, next[0]))


N, D = map(int, input().split())
arr = [[]  for _ in range(D+1)]
INF = int(1e9)
distance = [INF] * (D+1)

# 다음좌표로 가는길은 이전꺼 더하기 +1 에 가중치가 1이다
for i in range(D):
    arr[i].append((i+1, 1))

for _ in range(N):
    start, end, dist = map(int,input().split())
    # 마지막을 넘어가면 어차피 볼 필요없잖아?
    if end > D:
        continue
    arr[start].append((end, dist))

dijkstra(0)
print(distance[D])