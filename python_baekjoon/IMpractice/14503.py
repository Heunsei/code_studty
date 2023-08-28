N, M = map(int, input().split())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


room = [list(map(int, input().split())) for _ in range(N)]

r, c, d = map(int, input().split())

room[r][c] =