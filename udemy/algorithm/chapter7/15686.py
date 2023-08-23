from itertools import combinations

# 도시는 NxN
# r행 c열

def getdistance(h_p, c_p):
    return abs(h_p[0] - c_p[0]) + abs(h_p[1] - c_p[1])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
houses = []
chicken = []
# arr 을 순회하면서 1과 2의 좌표를 저장
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])
#print(houses)
#print(chicken)
spare = combinations(chicken, M)
ans = 987654321

for combi in spare:
    tot = 0
    for house in houses:
        tot += min(getdistance(house, chi) for chi in combi)
    ans = min(ans, tot)

print(ans)