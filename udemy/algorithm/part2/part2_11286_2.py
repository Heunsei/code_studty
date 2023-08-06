# 튜플로 안풀고 그냥풀기
import heapq as hq
import sys

input = sys.stdin.readline
min_heap = [] # 1,2,3,4...양수들만 최소힙
# 파이썬은 기본적으로 최소힙
max_heap = [] # 음수들만 따로 빼서 여기에서만 뺌 큰값부터 뺄거라 앞에서부터

for _ in range(int(input)):
    x = int(input())
    if x:
        if x > 0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, -x)
    else:
        if min_heap:
            if max_heap:
                if min_heap < abs(-max_heap[0]):
                    print(hq.heapop(min_heap))
                else:
                    print(-hq.heappop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)