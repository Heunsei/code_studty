import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
chk = [False for _ in range(N)]
min_value = sys.maxsize

def backtracking(depth, idx):
    global min_value
    if depth == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if chk[i] and chk[j]:
                    start += arr[i][j]
                elif not chk[i] and not chk[j]:
                    link += arr[i][j]
        min_value = min(min_value, abs(start-link))
        return
    for i in range(idx, N):
        if not chk[i]:
            chk[i] = True
            backtracking(depth+1, idx + 1)
            chk[i] = False


backtracking(0, 0)
print(min_value)