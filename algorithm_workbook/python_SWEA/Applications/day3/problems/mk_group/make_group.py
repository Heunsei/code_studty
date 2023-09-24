import sys
sys.stdin = open('input.txt')
def find_set(x):
    if parent[x] == x:
        return x
    return find_set(parent[x])

# def union(x,y):
#     x = find_set(x)
#     y = find_set(y)
#     if x == y:
#         return
#     else:
#         if x < y:
#             parent[y] = x
#         else:
#             parent[x] = y
def union(x,y):                     # x의 대표자를 찾아서 y의 대표자로 바꾸어줌
    parent[find_set(y)] = find_set(x)
    return x


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    graph = list(map(int,input().split()))
    for i in range(0, len(graph), 2):
        #print(graph[i], graph[i+1])
        union(graph[i],graph[i+1])

    result = set()
    for i in range(1, N + 1):
        result.add(find_set(i))
    print(f'#{tc} {len(result)}')
