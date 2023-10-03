N = int(input())
arr = []

for _ in range(N):
    a, b = map(str, input().split())
    a = int(a)
    arr.append((a,b))
arr.sort(key=lambda x: x[0] )

for i in arr:
    print(i[0], i[1])