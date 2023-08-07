import heapq as hq
import sys

input = sys.stdin.readline
pq = []
for _ in range(int(input())):
    x = int(input())
    if x :
        # 절댓값과 원소를 묶어서 비교
        # 절대값이 같으면 그중 x가 작은게 먼저 출력
        hq.heappush(pq, (abs(x), x))
    else:
        # print(hq.headpop(pq) if pq else 0)
        if pq:
            print(hq.heappop(pq)[1])
        else:
            print(0)
