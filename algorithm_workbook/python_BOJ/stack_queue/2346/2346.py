from collections import deque
# import sys
# sys.stdin = open('input.txt')

N = int(input())
b = deque(enumerate(map(int, input().split())))

# print(b)
ans = []

while b:
    idx, nxt = b.popleft()
    ans.append(idx + 1)
# 왼쪽으로 갈거면 양수
# 오른쪽으로 갈거면 음수
    if nxt > 0:
        b.rotate(-(nxt - 1))
    elif nxt < 0:
        b.rotate(-nxt)
print(' '.join(map(str, ans)))
