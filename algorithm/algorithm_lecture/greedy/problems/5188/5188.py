import sys
from collections import deque
sys.stdin = open('input.txt')

# 오른쪽, 아래
di = [0, 1]
dj = [1, 0]

def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N

def search():
    cnt = 0
    stk = deque()
    # 시작 좌표
    stk.append((0, 0))
    # 누적합을 저장 배열 chk에 초기값 넣어주기
    chk[0][0] = arr[0][0]
    while stk:
        i, j = stk.pop()
        cnt += 1
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            # 다음좌표가 알맞은 좌표면, 이전까지의 합 + 원본좌표값이랑 chk의 값이랑 비교
            if is_valid(ni, nj):
                if chk[ni][nj] == 0:
                    chk[ni][nj] = chk[i][j] + arr[ni][nj]
                else:
                    chk[ni][nj] = min(chk[ni][nj], arr[ni][nj] + chk[i][j])
                stk.append((ni, nj))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chk = [[0] * N for _ in range(N)]
    search()

    print('-----------arr------------')
    for i in arr:
        print(i)
    print('-----------chk-----------')
    for i in chk:
        print(i)
    print('--------------------------')
    print(f'#{tc} {chk[N - 1][N - 1]}')

