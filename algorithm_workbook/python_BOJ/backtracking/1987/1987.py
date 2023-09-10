import sys
input = sys.stdin.readline
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
alpha = set()
cnt = 0
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def is_valid(x, y):
    return 0 <= x < R and 0 <= y < C


def search(pos_i, pos_j, tmp):
    global cnt
    cnt = max(cnt, tmp)
    for k in range(4):
        ni = pos_i + di[k]
        nj = pos_j + dj[k]
        if is_valid(ni, nj) and graph[ni][nj] not in alpha:
            alpha.add(graph[ni][nj])
            search(ni, nj, tmp+1)
            alpha.remove(graph[ni][nj])


alpha.add(graph[0][0])
search(0, 0, 0)
print(cnt+1)
