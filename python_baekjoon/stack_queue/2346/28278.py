import sys
input = sys.stdin.readline

stack = []
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in arr:
    if len(i) >= 2:
        stack.append(i[1])
    if i[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif i[0] == 3:
        print(len(stack))

    elif i[0] == 4:
        if stack:
            print('0')
        else:
            print('1')
    elif i[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print('-1')

