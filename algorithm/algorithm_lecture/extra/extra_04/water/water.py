T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for tc in range(1, T+1):
    N, M = int(input().split())
    arr = [input() for _ in range(N)]
    