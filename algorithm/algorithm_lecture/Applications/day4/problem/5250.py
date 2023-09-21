from collections import deque
def is_valid(x,y):
    return 0 <= x < N and 0 <= y < N

def bfs():
    Q = deque()
    # x,y삽입
    Q.append((0,0))
    visited[0][0] = 0

    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 다음 좌표가 범위 내에 있고 목적지 좌표의 방문 표시값보다 작거나 같은 경우
            # 현재 위치가 다음 위치보다 낮거나 높을떄
            if is_valid(nx,ny) and visited[nx][ny] <= visited[N-1][N-1]:
                if arr[x][y] >= arr[nx][ny]:
                    if visited[nx][ny] > visited[x][y] + 1:
                        visited[nx][ny] = visited[x][y] +1
                        Q.append((nx,ny))
                else:
                    if visited[nx][ny] > visited[x][y] + 1 + (arr[nx][ny] - arr[x][y]):
                        visited[nx][ny] = visited[x][y] + 1 + (arr[nx][ny] - arr[x][y])
                        Q.append((nx, ny))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 가중치를 visited 에 기록
    max_val = sum(sum(arr, [])) + N**2
    visited = [[max_val] * N for _ in range(N)]

    bfs()
    print(arr[N-1][N-1])
