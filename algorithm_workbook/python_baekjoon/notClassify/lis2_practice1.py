# 5x5 차 배열
arr = [[1, 5, 3, 4, 7],
       [2, 7, 8, 9, 8],
       [7, 89, 1, 17, 25],
       [11, 71, 17, 77, 85],
       [87, 74,45,14,76]]

di = [0,1,0,-1]
dj = [1,0,-1,0]

for i in range(5):
    for j in range(5):
        tmp = []
        center = arr[i][j]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (-1 < ni < 5) and (-1 < nj < 5):
                tmp.append(arr[ni][nj])
        result = 0
        for m in tmp:
            result += abs(m -center)
print(result)