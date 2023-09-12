from collections import deque
N = int(input())
graph = [list(input()) for _ in range(N)]
visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


first = 0
second = 0


def is_valid(nx,ny):
    return 0 <= nx < N and 0 <= ny < N

# 파랑일때는 둘 다 올리고
# 빨강과 초록일때는 구분해서 count 를 올려야함
def bfs1(pos_x, pos_y):
    if visited1[pos_x][pos_y] == True:
        return
    global first
    dq = deque([(pos_x, pos_y)])
    visited1[pos_x][pos_y] = True
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_valid(nx,ny) and not visited1[nx][ny]:
                if graph[x][y] == 'R' or graph[x][y] == 'G':
                    if graph[nx][ny] == 'B':
                        continue
                if graph[x][y] == 'B':
                    if graph[nx][ny] != 'B':
                        continue
                dq.append((nx,ny))
                visited1[nx][ny] = True
    first += 1


def bfs2(pos_x, pos_y):
    if visited2[pos_x][pos_y] == True:
        return
    global second
    dq = deque([(pos_x, pos_y)])
    visited1[pos_x][pos_y] = True
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if is_valid(nx,ny) and not visited2[nx][ny] and graph[x][y] == graph[nx][ny]:
                dq.append((nx,ny))
                visited2[nx][ny] = True
    second += 1




for i in range(N):
    for j in range(N):
        bfs1(i,j)
        bfs2(i,j)

print(f'{second} {first}')