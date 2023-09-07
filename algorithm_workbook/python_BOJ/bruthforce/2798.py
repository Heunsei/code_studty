from itertools import combinations
# N은 카드개수
N, M = map(int, input().split())
cards = list(map(int, input().split()))
collect = []
for com in combinations(cards, 3):
    if sum(com) <= M:
        collect.append(sum(com))


print(max(collect))

