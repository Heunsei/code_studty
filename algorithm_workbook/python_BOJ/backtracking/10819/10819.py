N = int(input())
A = list(map(int, input().split()))
arr = [0] * N
visited = [False] * N
max_res = -987654321
def calculate(arr):
    tmp = 0
    for i in range(1, N):
        tmp += abs(arr[i-1] - arr[i])
    return tmp
def backtracking(depth, idx):
    global max_res
    if depth == N:
        max_res = max(max_res, calculate(arr))
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                arr[depth] = A[i]
                backtracking(depth + 1, i + 1)
                visited[i] = False
backtracking(0,0)
print(max_res)