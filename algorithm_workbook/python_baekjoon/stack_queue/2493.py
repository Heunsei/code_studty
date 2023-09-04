import sys
input = sys.stdin.readline
# 탑의 수를 나타내는 N
N = int(int(input()))
tower = list(map(int, input().split()))
stack = []

for i in range(N):
    if stack:
        while 1:
            if stack and stack[-1][1] < tower[i]:
                stack.pop()
            elif stack and stack[-1][1] > tower[i]:
                print(stack[-1][0] + 1, end=' ')
                break
            if not stack:
                print('0', end=' ')
                break
        stack.append((i, tower[i]))
    else:
        stack.append((i, tower[i]))
        print('0', end=' ')
        #print(stack)
