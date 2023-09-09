N = int(input())
number = list(map(int, input().split()))
# 받아올 데이터들을 하나씩 넣어서 관리
plus, minus, mul, divide = map(int, input().split())
max_res = -1e9
min_res = 1e9


def dfs(plus, minus, mul, divide, res, depth):
    global max_res, min_res
    if depth == N:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return
    # DFS 를 돌릴때 첫 시행때 1,2,3,4 번째 연산자를 어떤걸 먼저쓸지 결정하고
    # 각각의 분기점이 실행
    if plus:
        dfs(plus - 1, minus, mul, divide, number[depth] + res, depth + 1)
    if minus:
        dfs(plus, minus - 1, mul, divide, res - number[depth], depth + 1)
    if mul:
        dfs(plus, minus, mul - 1, divide, number[depth] * res, depth + 1)
    if divide:
        dfs(plus, minus, mul, divide - 1, int(res / number[depth]), depth + 1)

# 첫값을 넣고 시작하기때문에 깊이값이 1부터 시작해야함
dfs(plus, minus, mul, divide, number[0], 1)
print(max_res)
print(min_res)