from collections import deque

N, M = map(int, input().split())
to_find = deque(map(int, input().split()))
arr = deque(i for i in range(1, N+1))
cnt = 0
while to_find:
    #print(arr)
    #print(to_find)
    if arr[0] == to_find[0]:
        arr.popleft()
        to_find.popleft()
    elif arr.index(to_find[0]) <= (len(arr)//2):
        while arr[0] != to_find[0]:
            arr.append(arr.popleft())
            cnt += 1
    elif arr.index(to_find[0]) > (len(arr)//2):
        while arr[0] != to_find[0]:
            arr.appendleft(arr.pop())
            cnt += 1
print(cnt)