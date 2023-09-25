def perm(depth):
    global res
    if depth == N:
        a = ''
        for i in tmp:
            a += str(i)
        if int(a) > int(X):
            res = min(res, int(a))
    for next in range(N):
        if visited[next]:
            continue
        visited[next] = True
        tmp.append(arr[next])
        perm(depth+1)
        visited[next] = False
        tmp.pop()


X = input()
arr = []
for i in X:
    arr.append(int(i))
N = len(arr)
tmp = []
res = 987654321
visited = [False] * N
perm(0)
if res == 987654321:
    print(0)
else:
    print(res)