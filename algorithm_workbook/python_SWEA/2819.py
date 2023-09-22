# 격자판이 존재, 0부터 9사이의 숫자가 존재함
# 임의의 위치에서 시작해서 총 여섯번이동
# 각 칸에 적혀있는 숫자를 이어붙이자
def search(x, y, depth):
    if len(depth) == 7:
        result.add(depth)
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= 4:
            continue
        if ny < 0 or ny >= 4:
            continue

        search(nx, ny, depth + arr[nx][ny])



dx = [0,1,0,-1]
dy = [1,0,-1,0]

T = int(input())
for tc in range(1,T+1):
    arr = [input().split() for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            search(i,j, arr[i][j])
    print(f'#{tc} {len(result)}')