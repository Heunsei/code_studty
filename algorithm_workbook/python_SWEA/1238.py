from collections import deque
def bfs(start):
    q = [start]
    visited = [0] * 101
    visited[start] = 1
    max_number= start
    max_depth = 1
    while q:
        now = q.pop(0)
        for to in graph[now]:
            if visited[to]:
                continue
            visited[to] = visited[now] + 1
            if max_depth < visited[to] or ( max_depth == visited[to] and max_number < to):
                max_number = to
                max_depth = visited[to]
            q.append(to)
    return max_number

for tc in range(1, 11):
    N, S = map(int,input().split())
    arr = list(map(int, input().split()))
    graph = [[]  for _ in range(101)]
    for i in range(0, N, 2):
        f = arr[i]
        t = arr[i+1]
        graph[f].append(t)
    print(f'#{tc} {bfs(S)}')
