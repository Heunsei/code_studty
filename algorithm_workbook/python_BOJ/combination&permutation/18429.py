def perm(depth):
    global res
    if depth == N:
        a = 500
        for i in tmp:
            a += (i-K)
            if a < 500:
                return
        res += 1
    for next in range(N):
        if visited[next]:
            continue
        visited[next] = True
        tmp.append(work_out[next])
        perm(depth+1)
        visited[next] = False
        tmp.pop()

# N개의 운동기구(날짜) 1일마다 K만큼 중량감소
N, K = map(int, input().split())
work_out = list(map(int, input().split()))
visited = [False] * N
res = 0
tmp = []
perm(0)
print(res)