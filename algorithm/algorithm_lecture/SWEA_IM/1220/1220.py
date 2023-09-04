# magnetic
import sys
sys.stdin = open('input.txt')

def is_vail(i, j):
    return 0 <= i < N and 0 <= j < N

for tc in range(1,11):
    N = int(input())
    # 1은 N극 2는 S극
    # 1은 아래로 2는 위로
    arr = [list(map(int, input().split())) for _ in range(100)]
    attach = []
    # 위 / 아래
    di = [-1, 1]
    dj = [0, 0]
    # 1의 경우 아래에 무언가 있으면 움직이지 않음
    # 2의 경우 위에 무언가가 있으면 움직이지 않음
    count = 0
    i = 0
    while i < 100:
        for i in range(N):
            for j in range(N):
                # 아래로 가야하는 N극 일때
                if arr[i][j] == 1:
                    ni = i + di[1]
                    nj = j + dj[1]
                    
                    if is_vail(ni, nj) and arr[ni][nj] != 2:
                        arr[ni][nj] = 1
                        # 위가 S극 일때
                    # if is_vail(ni, nj) and arr[ni][nj] == 2:
                    #     # N극 / S극
                    #     attach.append((i, j, ni, nj))
                    if not is_vail(ni, nj):
                        arr[i][j] = 0
                # 위로 가야하는 S극 일때
                elif arr[i][j] == 2:
                    ni = i + di[0]
                    nj = j + dj[0]
                    if is_vail(ni, nj) and arr[ni][nj] != 1:
                        arr[ni][nj] = 2
                    # if is_vail(ni, nj) and arr[ni][nj] == 1:
                    #     # N극 / S극
                    #     attach.append((ni, nj, i, j))
                    if not is_vail(ni, nj):
                        arr[i][j] = 0
        i += 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if arr[i+1][j] == 2:
                    count += 1
            elif arr[i][j] == 2:
                if arr[i-1][j] == 1:
                    count += 1

    print(f'#{tc} {count // 2}')
