def perm(depth):
    acc = ''
    if depth == k:
        for i in tmp:
           acc += str(i)
        res.append(acc)
        return
    for next in range(n):
        if visited[next]:
            continue
        visited[next] = True
        tmp.append(arr[next])
        perm(depth+1)
        visited[next] = False
        tmp.pop()

n = int(input())
# k개의 숫자를 뽑을 것
k = int(input())
arr = []
tmp = []
res = []
visited = [False] * n
for _ in range(n):
    arr.append(int(input()))
perm(0)
print(len(set(res)))