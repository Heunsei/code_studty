import sys
sys.stdin = open('input.txt')

di = [1, 0, 0]
dj = [0, -1, 1]

def serch(arr, i, j):
    check = [[0]*100 for _ in range(100)]
    to_return = j
    check[i][j] = 1
    while i != 99:
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]
            # 좌표값 이동
            if 0 <= ni < 100 and 0 <= nj <100 and arr[ni][nj] and check[ni][nj] == 0:
                # 좌표값이동
                i, j = ni, nj
                check[ni][nj] = 1

    if arr[i][j] == 2:
        return to_return
    else:
        return '실패'

for tc in range(1, 11):
    T = int(input())
    di = [0, 0, 1]
    dj = [1, -1, 0]

    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[0][i] == 1:
            result = serch(arr, 0, i)
        if result != '실패':
            break
    print(f'#{tc} {result}')



