from collections import deque
N, K = map(int, input().split())
dq = deque(i for i in range(1, N+1))
ans = []
while dq:
    dq.rotate(-K + 1)
    ans.append(dq.popleft())
print('<', end='')

for i in range(len(ans)-1):
    print(ans[i], end=', ')

print(ans[-1],end='')
print('>',end='')