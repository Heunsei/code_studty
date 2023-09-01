def perm(now, r):
    global result
    val = int(''.join(cards))

    if val in visited[now]:
        return
    visited[now].add(val)
    if now == r:
        if result < val:
            result = val
    else:
        for i in range(N-1):
            for j in range(i + 1, N):
                cards[i], cards[j] = cards[j], cards[i]
                perm(now + 1, r)
                cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for tc in range(1, T+1):
    memo = [[0] * 720 for _ in range(11)]
    cards, r = list(map(int, input().split()))
    cards = list(str(card))
    visited = [set() for _ in range(11)]
    N = len(cards)
    result = 0

