def search(depth):
    global res
    if sum(candidate) > res:
        return
    if depth == N:
        res = min(sum(candidate), res)
        print(candidate)
        return
    for i in range(N):
        if visited[i]:
            continue
        candidate.append(graph[depth][i])
        visited[i] = True
        search(depth+1)
        candidate.pop()
        visited[i] = False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    candidate = []
    visited = [False] * N
    res = 987654321
    search(0)
    print(f'#{tc} {res}')