import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
member = list(range(N))
num_of_team = N // 2
min_value = sys.maxsize

for link in combinations(member, num_of_team):
    value_1 = 0
    value_2 = 0
    start = list(set(member) - set(link))
    for i in combinations(start, 2):
        value_1 += arr[i[0]][i[1]]
        value_1 += arr[i[1]][i[0]]
    for j in combinations(link, 2):
        value_2 += arr[j[0]][j[1]]
        value_2 += arr[j[1]][j[0]]
    min_value = min(min_value, abs(value_2 - value_1))

print(min_value)

