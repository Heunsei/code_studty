# 달팽이
from pprint import pprint
di = [0,1,0,-1]
dj = [1,0,-1,0]

T = int(input())
snail = [[0]*T for _ in range(T)]


i = 0
j = 0
dir = 0
count = 1
snail[i][j] = count

while count < T**2:
    ni = i + di[dir]
    nj = j + dj[dir]
    print(ni,nj)
    if (0 <= ni < T) and (0 <= nj < T) and snail[ni][nj] == 0:
        count += 1
        snail[ni][nj] = count
        i,j = ni, nj
    else :
        dir += 1
        if dir >= 4:
            dir = 0
for i in snail:
    print(i)
    

        
