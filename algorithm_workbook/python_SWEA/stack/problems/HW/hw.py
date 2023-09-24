def DFS(start, end):
    for nxt in range(100):
        if adj[start][nxt] and not visited[nxt]:
            visited[nxt] = True
            if nxt == end:
                global is_there
                is_there = True
                return
            DFS(nxt, end)


for _ in range(10):
    # 테스트 케이스 번호, 길의 개수
    tc, N = map(int, input().split())
    # 간선을 저장할 인접행렬
    adj = [[0] * 100 for _ in range(100)]
    # 간선 정보
    data = list(map(int, input().split()))
    visited = [False] * 100
    is_there = False

    for i in range(0, N*2, 2):
        adj[data[i]][data[i+1]] = 1

    DFS(0, 99)
    if is_there:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')