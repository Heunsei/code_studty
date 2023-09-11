arr = [1,2,3,4,5]
N = len(arr)
visited = [False] * N
pArr = []
M = 2 # 우리가 구할 후보군의 길이

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, pArr)))
        return
    for i in range(N):
        if visited[i]:
            continue
        pArr.append(arr[i])
        visited[i] = True
        dfs(depth+1)
        pArr.pop()
        visited[i] = False
dfs(0)
