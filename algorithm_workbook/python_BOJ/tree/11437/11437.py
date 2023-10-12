# N개의 정점으로 이루어진 트리
# 각정점은 1부터 N까지 번호가 매겨져 있으며 루트노드는 항상1번이다

from collections import deque
N = int(input())
tree = [[] for _ in range(N+1)]

def find(to_find):
    dq = deque()
    dq.append(([1], 1))
    while dq:
        path, cur = dq.popleft()
        if cur == to_find:
            return path
        for next in tree[cur]:
            if tree[cur]:
                tmp = path + [next]
                dq.append((tmp, next))


for _ in range(N-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    a_parents = find(a).reverse()
    b_parents = find(b).reverse()
    for i in a_parents:
        if i in b_parents:
            print(i)
