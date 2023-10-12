import sys
sys.setrecursionlimit(int(1e5))
N = int(input())
tree = [[] for _ in range(N+1)]
parent = [0] * (N+1)
d = [0] * (N+1)
calculated = [0] * (N+1)

def dfs(x, depth):
    calculated[x] = True
    d[x] = depth
    # y는 x의 자식노드들
    for y in tree[x]:
        if calculated[y]:
            continue
        parent[y] = x
        dfs(y, depth+1)


# 최소공통조상 알고리즘
def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1,0)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
