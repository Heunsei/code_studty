def perm(depth):
    if depth == N:
        print(*tmp)
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                tmp[depth] = arr[i]
                perm(depth+1)
                visited[i] = False

N = int(input())
arr = [i for i in range(1,N+1)]
tmp = [0] * N
visited = [False] * N
perm(0)