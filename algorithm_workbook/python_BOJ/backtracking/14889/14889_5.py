import sys
input = sys.stdin.readline
# 조합만들기
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [False] * N
min_value = sys.maxsize

def backtracking(depth, idx):
    global min_value
    if depth == N//2:
        power1, power2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    power1 += arr[i][j]
                else:
                    power2 += arr[i][j]
        min_value = min(min_value, abs(power2 - power1))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            backtracking(depth + 1, i + 1)
            visited[i] = False


backtracking(0,0)
print(min_value)