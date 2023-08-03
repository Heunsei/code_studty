# 달팽이
from pprint import pprint

T = int(input())
snail = [[0]*T for _ in range(T)]

di = [0,1,0,-1]
dj = [1,0.-1,0]

i = 0
j = 0
count = 1
current_position = snail[i][j]
while True:

    if snail[i][j] == 0:
        snail[i][j] = count
        count +=1
    for k in range(4):
        i += di
        j += dj
        pass

print(snail)
        
