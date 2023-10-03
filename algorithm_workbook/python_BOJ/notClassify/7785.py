N = int(input())
arr = []
for _ in range(N):
    a, b = input().split()
    if b == 'enter':
        arr.append(a)
    else:
        arr.remove(a)

arr.sort(reverse=True)
for i in arr:
    print(i)