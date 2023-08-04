# 500000넣으면 연산 오래걸림
N = int(input())
arr = [*range(1, N+1)]
while len(arr) > 1:
    arr.pop(0)
    arr.append(arr.pop(0))
print(arr.pop())