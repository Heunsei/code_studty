import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
pArr = [0] * M
visited = [False] * N


def duplicate_permutation(depth):
    if depth == M:
        is_upper = True
        for i in range(1, M):
            if pArr[i-1] > pArr[i]:
                return
        if is_upper:
            print(' '.join(map(str, pArr)))
        return
    for i in range(N):
        pArr[depth] = arr[i]
        if depth >= 1 and pArr[depth-1] > pArr[depth-1]:
            return
        duplicate_permutation(depth+1)


duplicate_permutation(0)