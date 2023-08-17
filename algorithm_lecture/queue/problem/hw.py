from collections import deque
for _ in range(10):
    tc = int(input())
    dq = deque()
    dq.extend(input().split())
    t = 1
    while True:
        a = int(dq.popleft()) - t

        if a <= 0:
            a = 0
            dq.append(a)
            break

        dq.append(a)
        t += 1
        if t >= 6:
            t = 1

    print(f'#{tc}', *dq)
