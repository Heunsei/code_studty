# 연산자 끼워넣기
# 함수를 사용할때 결과값을 함수로 넘겨 누적할 수 있다는 것을 기억하자
N = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_val = -10000000000
min_val = 10000000000


def backtracking(plus, minus, mul, div, sum, depth):
    global max_val, min_val
    if depth == N:
        max_val = max(max_val, sum)
        min_val = min(min_val, sum)
    else:
        if plus:
            backtracking(plus-1, minus, mul, div, numbers[depth] + sum, depth+1)
        if minus:
            backtracking(plus, minus-1, mul, div, sum - numbers[depth], depth+1)
        if mul:
            backtracking(plus, minus, mul-1, div, numbers[depth] * sum, depth+1)
        if div:
            backtracking(plus, minus, mul, div-1, int(sum / numbers[depth]), depth+1)

backtracking(plus, minus, mul, div, numbers[0], 1)
print(max_val)
print(min_val)