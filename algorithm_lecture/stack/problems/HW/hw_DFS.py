def DFS(start):
    visited[start] = 1
    for nxt in range(100):
        if adj[start][nxt] == 1 and visited[nxt] == 0:
            visited[nxt] = 1
            if nxt == 99:
                global is_goal
                is_goal = True
                return
            DFS(nxt)


for _ in range(1, 11):
    adj = [[0]*100 for _ in range(100)]
    tc, n = map(int, input().split())
    # 간선정보 받아오기
    node = list(map(int, input().split()))
    visited = [0] * 100
    is_goal = False
    # 간선표시
    for i in range(0, n*2, 2):
        a, b = node[i], node[i+1]
        adj[a][b] = 1

    DFS(0)

    if is_goal == True:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')