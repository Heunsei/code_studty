# 탈주범 검거
# 표에있는 파이프간의 규칙을 찾는게 중요한 문제

# 탐색 가능 범위
tunnel = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}


# 좌표 x,y
# 이동 시간 cnt
def bfs(x, y, cnt):
    global result
    q = [(x, y, cnt)]
    visited[x][y] = 1
    while q:
        x, y, cnt = q.pop(0)
        if cnt == L:    # 현재 조사 하는데 걸린 시간이 최대 시간이 되면 종료
            return
        result += 1
        for dx, dy in tunnel[arr[x][y]]:
            nx = x + dx
            ny = y + dy
            # 조사 범위 체크
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] and not visited[nx][ny]:
                for cx, cy in tunnel[arr[nx][ny]]:
                    if dx + cx == 0 and dy + cy == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt + 1))
                        break


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L, = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    result = 0
    bfs(R, C, 0)

