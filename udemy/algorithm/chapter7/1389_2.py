# 케빈 베이컨
# BFS를 이용해서 각각의 노드와의 거리를 전부 더한 후 한 리스트에 관리하고
# 그중 가장 작은값의 index를 출력하는 문제
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
result = []

ans = (-1, 987654321)

def BFS(start,end):
    dq = deque()
    dq.append((start, 0))
    visited = [False] * N
    visited[start] = True
    while dq:
        now, d = dq.popleft()
        if now == end:
            return d
        nd = d + 1
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                dq.append((nxt, nd))

# i를 순회시키면서 end값을 변화시키고 값을 result에 누적
def get_result(start):
    tot = 0
    for i in range(N):
        if i != start:
            tot += BFS(start, i)
    return tot

for _ in range(M):
    # 양방향 리스트니까 그래프에 양쪽을 저장
    a, b = map(lambda x: x-1, map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    result.append(get_result(i))

# result의 인덱스와 값을 받아오고
# ans의 1번째 값 (총합을나타냄)이 작으면 ans를 변경
for i, v in enumerate(result):
    if ans[1] > v:
        ans = (i, v)
# 값을 받아올 떄 -1만큼 줄여서 받아왔으니(인덱스로 그대로 받아옴) +1 해서 넘겨줌
print(ans[0] + 1)