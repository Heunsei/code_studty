import sys
input = sys.stdin.readline

K = int(input())
arr = []
for _ in range(K):
    a = int(input())
    if a != 0:
        arr.append(a)
    else:
        arr.pop()

print(sum(arr))