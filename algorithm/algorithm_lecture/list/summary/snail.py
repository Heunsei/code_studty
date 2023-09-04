T = int(input())

arr = [[0]*T for _ in range(T)]

i, j = 0, 0
count = 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 방향을 컨트롤 할 변수
k = 0
arr[i][j] = count
while count < T ** 2:
    ni = i + di[k]
    nj = j + dj[k]
    # 다음 위치로 옮겨봤을때 값이 범위 안에 있고, 다음값이 0이면 색칠하고 계속진행
    if 0 <= ni < T and 0 <= nj < T and arr[ni][nj] == 0:
        count += 1
        arr[ni][nj] = count
        i, j = ni, nj
    # 다음값이 범위밖에 없네? 방향을 바꿔
    else:
        k += 1
        if k >= 4:
            k = 0

print(arr)

