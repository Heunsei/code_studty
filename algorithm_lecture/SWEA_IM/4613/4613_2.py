import sys
sys.stdin = open('input.txt')


def first_blue(arr, color):
    min_blue = 0
    min_idx = 0
    for i in range(1,len(arr)-1):
        if arr[i].count(color) > min_blue:
            min_blue = arr[i].count(color)
            min_idx = i
    return min_idx

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    blue_idx = first_blue(arr, 'B')
    print(blue_idx)
    for i in arr:
        w_count = i.count('W')
        b_count = i.count('B')
        r_count = i.count('R')
        print(w_count, b_count, r_count)
    print('------------')

    for i in range(blue_idx):
        for j in range(i, blue_idx):
            w_count = arr[i].count('W')
            print('w_c', M - w_count)

    #
