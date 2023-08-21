# 백트래킹은 아직 마다마다다


board = [list(map(int, input().split())) for _ in range(10)]
# 각각의 색종이는 5개 까지만
# 1 2 3 4 5의 정사각형 색종이 보유
# 하나씩 넣어보고 분기를 작성하는 백트래킹 방법
ans = 25  # 충분히 큰 값
paper = [0] * 6  # 1부터 5까지 사용한 색종이의 수


def is_possible(y, x, sz):
    # 다씀
    if paper[sz] == 5:
        return False
    # 범위 체크
    if y + sz > 10 or x + sz > 10:
        return False

    for i in range(sz):
        for j in range(sz):
            if board[y + i][x + j] == 0:
                return False
    return True


def mark(y, x, sz, v):
    for i in range(sz):
        for j in range(sz):
            board[y+i][x+j] = v
    # v가 1일때
    if v:
        paper[sz] -= 1
    else:
        paper[sz] += 1


# 좌상단에서 시작해서 하나씩 오른쪽으로 진행
def backtracking(i, j):
    global ans
    if i == 10:
        ans = min(ans, sum(paper))
        return

    if j == 10:
        backtracking(i + 1, 0)
        return

    if board[i][j] == 0:
        backtracking(i, j + 1)
        return

    for sz in range(1, 6):
        if is_possible(i, j, sz):

            mark(i, j, sz, 0)
            backtracking(i, j+1)
            # 다끝나고 원상복구
            mark(i, j, sz, 1)


backtracking(0, 0)
print(-1 if ans == 25 else ans)
