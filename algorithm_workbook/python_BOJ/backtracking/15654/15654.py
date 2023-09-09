N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []


def permutation(depth):
    if depth == M:
        print(' '.join(map(str, res)))
        return
    for i in range(N):
        if arr[i] in res:
            continue
        res.append(arr[i])
        permutation(depth+1)
        res.pop()


permutation(0)

