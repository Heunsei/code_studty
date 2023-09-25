from collections import deque


def check_end(x, y):
    if x == 0 or y == 0:
        return True
    elif x == R - 1:
        return True
    elif y == C - 1:
        return True
    return False


def is_valid(x, y):
    return 0 <= x < R and 0 <= y < C


def bfs(jihun_x, jihun_y):
    global res
    jihun = deque()
    jihun.append((jihun_x, jihun_y, 0))
    # 지훈이를 먼저 옮겨 놓자
    while jihun:
        crt_x, crt_y, acc = jihun.popleft()
        if graph[crt_x][crt_y] == 'F':
            continue
        if check_end(crt_x, crt_y):
            res = min(acc, res)
        for k in range(4):
            nx = crt_x + dx[k]
            ny = crt_y + dy[k]
            if is_valid(nx, ny) and graph[nx][ny] == '.':
                nxt_acc = acc + 1
                graph[nx][ny] = 'J'
                jihun.append((nx, ny, nxt_acc))
        # fire 의 1차 움직임을 구현해야함
        while fire:
            cur_fire_x, cur_fire_y = fire.popleft()
            for k in range(4):
                nxt_fire_x = cur_fire_x + dx[k]
                nxt_fire_y = cur_fire_y + dy[k]
                if is_valid(nxt_fire_x, nxt_fire_y):
                    if graph[nxt_fire_x][nxt_fire_y] == 'J' or graph[nxt_fire_x][nxt_fire_y] == '.':
                        fire.append((nxt_fire_x, nxt_fire_y))
                        graph[nxt_fire_x][nxt_fire_y] = 'F'

    print("IMPOSSIBLE")


# 미로에서 탈출하기
dx = [-1, 1, 0, 0]
dy = [0, 0, - 1, 1]
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
# . 지나갈 수 있는 공간 / J 미로 초기 공간 / F 불이 난 공간 / # 벽
fire = deque()
res = 987654321
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'J':
            j_x, j_y = i, j
        if graph[i][j] == 'F':
            fire.append((i, j))
bfs(j_x, j_y)
