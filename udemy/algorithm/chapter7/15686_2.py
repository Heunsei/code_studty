from itertools import combinations

N, M = map(int, input().split())

house = []
chicken = []

for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            house.append((i, j))
        elif v == 2:
            chicken.append((i, j))

# 도시의 치킨 거리의 최소값
ans = 987654321

def get_dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])

for combi in combinations(chicken, M):
    tot = 0
    for h in house:
        tot += min(get_dist(h, chi) for chi in combi)
    ans = min(ans, tot)

print(ans)