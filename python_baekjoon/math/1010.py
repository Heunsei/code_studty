# 다리 놓기
import sys
import math
input = sys.stdin.readline

# def combination(n, r, s):
#     global count
#     if r == 0:
#         count += 1
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = tmp[i]
#             combination(n, r-1, i + 1)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    tmp = [i for i in range(M)]
    # comb = [0] * M
    # count = 0
    # combination(M, N, 0)
    # print(count)
    ans = math.factorial(M) / (math.factorial(M-N) * math.factorial(N))
    print(int(ans))