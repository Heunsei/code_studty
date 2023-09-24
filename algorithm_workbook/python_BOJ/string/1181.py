N = int(input())
arr = []
for i in range(N):
    arr.append(input())

set_list = set(arr)
arr = list(set_list)
arr.sort()
arr.sort(key = len)
set(arr)
for i in arr:
    print(i)