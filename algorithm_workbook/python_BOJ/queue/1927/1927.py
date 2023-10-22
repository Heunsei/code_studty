# 최소 힙
import heapq
import sys
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    a = int(input())
    if a != 0:
        heapq.heappush(heap,a)
    else:
        if not heap:
            print(0);
        else:
            print(heapq.heappop(heap))