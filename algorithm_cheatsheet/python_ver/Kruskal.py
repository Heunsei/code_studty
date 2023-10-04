# 모든 간선들 중 비용이 가장 적은 걸 우선으로 고르자
# 정점에 비해 간선이 적은 희소 그래프 에서는 크루스칼 알고리즘 이 적합
# 정점에 비해 간선이 많은 밀집 그래프 에서는 프림 알고리즘 이 적합

V, E = map(int, input().split())
# 저장방법이 조금 다름
# 시작정점, 도착점, 가중치를 모두 edge에 때려넣고 시작
edge = []
for _ in range(E):
    start, to, weight = map(int, input().split())
    edge.append([start, to, weight])

edge.sort(key=lambda x: x[2])
# 사이클 발생 여부를 union - find 로 해결
parents = [i for i in range(V)]


def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


# 현재 방문한 정점의 수
cnt = 0
sum_weight = 0
for f,t,w in edge:
    # 사이클 발생 x
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f,t)
        if cnt == V:
            break

