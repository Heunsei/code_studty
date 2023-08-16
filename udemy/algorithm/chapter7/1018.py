N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

# N이 8 M이 8이라면 0부터 8칸 검사할거고 8줄 검사할것
ans = 64  # 전부 b로 채워져있을때 절반정도만 바꿔도 되니까 최대값을 64로 설정

# 좌상단의 좌표와 색
def fill(y, x, bw):
    global ans
    cnt = 0
    for i in range(8):
        for j in range(8)
            if (i + j) % 2:
                if board[y + i][x + j] == bw:
                    cnt += 1
            else:
                if board[y + i][x + j] != bw:
                    cnt += 1
    ans = min(ans, cnt)

for i in range(N-7):
    for j in range(M-7):
        fill(i, j, 'B')
        fill(i, j, 'W')