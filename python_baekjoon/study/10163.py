# 색종이의 면적을 구하는 문제
from pprint import pprint
T = int(input())
for tc in range(1, 1+T):
    # sample에 좌표값들을 받아옴
    sample = [list(map(int, input().split())) for _ in range(T)]
    arr = [[0]*1001 for _ in range(1001)]
    # [0, 0, 10, 10]
    # [2, 2, 6, 6]
    # j,i 으로부터 j만큼 10 i만큼 10
    for m in range(T):
        for i in range(sample[m][0], sample[m][0] + sample[m][2]):
            for j in range(sample[m][1], sample[m][1]+ sample[m][3]):
                arr[i][j] = m + 1

    tmp = [0] * (T+1)

    for i in range(1001):
        for j in range(1001):
            if arr[i][j]:
                tmp[arr[i][j]] += 1

    for i in range(1, T+1):
        print(tmp[i])







