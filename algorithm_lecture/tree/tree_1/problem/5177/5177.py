# 이진 힙

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N + 1)
    last = 1
    for i in range(N):
        if tree[i] == 0:
            tree[last] = arr[i]
        else:
            last += 1
            tree[last] = arr[i]

            child = last
            parent = child // 2

            while parent >= 1 and tree[parent] > tree[child]:
                tree[parent], tree[child] = tree[child], tree[parent]
                child = parent
                parent = child //2
    ans = 0
    last_node = N // 2

    while last_node != 0:
        ans += tree[last_node]
        last_node //= 2

    print(f'#{tc} {ans}')
