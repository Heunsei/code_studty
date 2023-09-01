import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
pArr = []
visited = [False] * N

def dfs(depth, index):
    if depth == M:
        print(' '.join(map(str, pArr)))
        return
    for i in range(index, N+1):
        pArr.append(i)
        dfs(depth+1, i)
        pArr.pop()
dfs(0,1)