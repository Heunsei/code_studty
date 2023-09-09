# 부분 수열의 합
# 왜맞음?????????????????
N, S = map(int, input().split())
arr = list(map(int, input().split()))
res = 0


def perm(depth, val):
    global res
    if depth == val:
        if sum(tmp) == S:
            res += 1
    else:
        for i in range(N):
            if visited[i]:
                return
            visited[i] = True
            tmp[depth] = arr[i]
            perm(depth+1, val)
            visited[i] = False


for i in range(1, N+1):
    visited = [0] * N
    tmp = [0] * i
    perm(0, i)
print(res)