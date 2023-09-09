arr = [1, 2, 3, 4, 5]       # 후보를 찾을 배열
N = 3                   # 후보의 수

res = [0] * N       # result
check = [False] * len(arr)     # checker


def perm(depth):
    if depth == N:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(len(arr)):
            if check[i]:
                continue
            check[i] = True
            res[depth] = arr[i]
            perm(depth+1)
            check[i] = False


perm(0)