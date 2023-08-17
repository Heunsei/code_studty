from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    dq = deque()
    dq.extend(map(int, input().split()))
    #print(dq)
    for _ in range(M):
        a = dq.popleft()
        dq.append(a)
    print(f'#{tc} {dq[0]}')
