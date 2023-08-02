# 100x100 2차원 배열 생성
import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    test = [list(map(int, input().split())) for _ in range(100)]
    max_val = 0

    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += test[i][j]
            if tmp > max_val:
                max_val = tmp

    for j in range(100):
        tmp = 0
        for i in range(100):
            tmp += test[i][j]
            if tmp > max_val:
                max_val = tmp
    tmp = 0
    for i in range(100):
        tmp = 0
        tmp += test[i][i]
        if tmp > max_val:
            max_val = tmp
        tmp = 0

    tmp = 0
    for i in range(100):
        tmp = 0
        tmp += test[i][100-1-i]
        if tmp > max_val:
            max_val = tmp
        tmp = 0

    print(f'#{T} {max_val}')