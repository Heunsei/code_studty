import heapq
tc = 1
while True:
    N = int(input())
    if N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 987654321
    dp = [[INF] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    def search():
        pq = []
        heapq.heappush(pq, (arr[0][0], 0, 0))
        dp[0][0] = 0
        while pq:
            cost, x, y = heapq.heappop(pq)
            if x == N-1 and y == N-1:
                print(f'Problem {tc}: {dp[x][y]}')
                break
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0<= ny < N:
                    new_cost = cost + arr[nx][ny]
                    if new_cost < dp[nx][ny]:
                        dp[nx][ny] = new_cost
                        heapq.heappush(pq,(new_cost, nx, ny))

    search()
    tc += 1