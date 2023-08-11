# 미로찾기 문제 혼자구현
from collections import deque

def isValid(i,j):
    return 0 <= i < N and 0 <= j < M


# 시작 값 고정
# 마지막 위치 찾아갔을때 가장작은 횟수 출력

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

def BFS():
    # 체커생성
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    # 덱에 시작위치 저장
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        i, j, d = dq.popleft()
        if i == N-1 and j == M-1:
            return d
        nd = d + 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # string이니까 '1'로 검사해야함
            if isValid(ni, nj) and not chk[ni][nj] and board[ni][nj] == '1':
                chk[ni][nj] = True
                dq.append((ni, nj, nd))



# 미로찾기 류는 BFS로 구현

N, M = map(int, input().split())
board = [input() for _ in range(N)]
print(BFS())