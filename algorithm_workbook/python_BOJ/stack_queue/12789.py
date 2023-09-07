T = int(input())
cnt = 1
arr = list(map(int, input().split()))
stack = []

while arr:
    if stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1
        continue

    if arr[0] == cnt:
        arr.pop(0)
        cnt += 1
    else:
        stack.append(arr.pop(0))
    #print(stack)


while stack:
    if stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1
    else:
        break

if stack:
    print("Sad")
else:
    print("Nice")