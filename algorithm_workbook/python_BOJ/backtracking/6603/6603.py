# 로또
import sys
sys.stdin = open('input.txt')


def comb(depth, idx):
    global arr
    if depth == 6:
        print(' '.join(map(str,tmp)))
        return
    for i in range(idx, len(arr)):
        tmp.append(arr[i])
        comb(depth+1, i+1)
        tmp.pop()


while True:
    tmp = []
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    arr.pop(0)
    comb(0, 0)
    print()
