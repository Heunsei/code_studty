N = int(input())
number = list(input())
plus, minus, mul, div = map(int, input().split())
operator = []
for i in range(plus):
    operator.append('+')
for i in range(minus):
    operator.append('-')
for i in range(mul):
    operator.append('*')
for i in range(div):
    operator.append('/')


# 기호끼리의 조합


