arr = [[1,2,3,4,5],
       [5,7,51,23,63],
       [76,53,11,53,23],
       [54,31,45,53,76],
       [55,98,68,81,43]]

di = [1,1,-1,-1]
dj = [1,-1,-1,1]

for i in range(5):
    for j in range(5):
        tmp = []
        center = arr[i][j] 
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if (-1<ni<5) and (-1<nj<5):
                tmp.append(arr[ni][nj])
        if sum(tmp) > 200:
            print(i,j)
        
