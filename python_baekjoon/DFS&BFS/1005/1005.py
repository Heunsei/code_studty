from collections import deque
import sys
input = sys.stdin.readline
#sys.stdin = open('input.txt')
T = int(input())

def topology():
    dq = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            dq.append(i)
            dp[i] = delay[i]
    while dq:
        nxt = dq.popleft()
        for i in arr[nxt]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[nxt] + delay[i])
            if indegree[i] == 0:
                dq.append(i)

for _ in range(T):
    N, K = map(int, input().split())
    delay = [0] + list(map(int, input().split()))
    arr = [[] for _ in range(N+1)]
    dp = [0] * (N+1)
    indegree = [0] * (N+1)
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a].append(b)
        indegree[b] += 1
    W = int(input())
    topology()
    print(dp[W])