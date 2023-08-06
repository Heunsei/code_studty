# 배열의 탐색 방향을 설정할 좌표들
di = [0, 0, 1]
dj = [1, -1, 0]

# 배열이랑 시작좌표 받아와서 탐색 시작하기
# i랑 j을 조건받아서 시작할거라 바로 설정해도 될듯
def serch(arr, i, j):
    original_j= j
    check_list = [[0]*100 for _ in range(100)]
    check_list[i][j] = 1
    while i != 99:
        for k in range(3):
            ni = i + di[k]
            nj = j + dj[k]
            # 다음 좌표의 값이 이렇다면
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] and check_list[ni][nj]==0:
                # 좌표를 변경
                i, j = ni, nj
                # check_list 를 1더하고
                check_list[ni][nj] = 1

    if arr[i][j] == 2:
        return original_j
    else:
        return '실패'

for _ in range(1, 11):
    tc = int(input())
    # 100x100 배열생성
    array = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100):
        if array[0][j] == 1:
            result = serch(array, 0, j)
        if result != '실패':
            break
    print(f'#{tc} {result}')