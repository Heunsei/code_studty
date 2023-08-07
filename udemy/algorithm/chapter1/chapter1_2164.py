# 풀었지만 시간초과로 실패

from collections import deque
#ddq = deque(range(1,N+1))

dq = deque()
N = int(input())
for i in range(1, N+1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.popleft())

