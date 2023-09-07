import math
# 어린왕자
T = int(input())
for tc in range(1, T+1):
    count = 0
    # 출발점 도착점
    j1, i1, j2, i2 = map(int, input().split())
    # 행성의 개수 N
    N = int(input())
    for i in range(N):
        y, x, r = map(int, input().split())
        # 출발점과 도착점이 원 안에 있는지 판별
        start = math.sqrt(abs(y - j1)**2 + abs(x - i1)**2)
        end = math.sqrt(abs(y - j2)**2 + abs(x - i2)**2)

        #print(start, end)
        if start < r and end < r:
            continue
        elif start > r and end > r:
            continue
        elif start < r and end > r:
            #print(count)
            count += 1
        elif start > r and end < r:
            count += 1
    print(count)