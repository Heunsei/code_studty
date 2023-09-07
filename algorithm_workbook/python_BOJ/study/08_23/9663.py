def adjacent(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i:
            return False
    return True


def dfs(x):
    global result
    if x == N:
        result += 1
    else:
        for i in range(N):
            col[x] = i
            if adjacent(x):
                dfs(x + 1)


N = int(input())
col = [0] * N
result = 0
dfs(0)
print(result)
