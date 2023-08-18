from collections import deque
# 복습 필요
# 각 값에서 출발해서 count가 가장 작은 start를 찾기
N, M = map(int, input().split())
adj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

kevin = []
# 답을 튜플에 넣어 인덱스랑 같이 관리
ans = (-1, 987654321)

def bfs(start,goal):
    # 방문 노드 체크
    chk = [False] * N
    # 첫 시작은 True로
    chk[start] = True
    dq = deque()
    # dq에 넣는건 count값과 start 노드
    dq.append((start, 0))
    # dq가 빌 때 까지
    while dq:
        # popleft 해서 start 와 끝값 받아오기
        now, d = dq.popleft()
        # 도착하면 count 값인 d 반환
        if now == goal:
            return d
        # count += 1
        nd = d + 1
        for nxt in adj[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, nd))


def get_kevin(start):
    tot = 0
    # start를 주어지고 안에있는 goal 을 순회하면서
    # tot 에 bfs 가 반환하는 d 를 누적
    for i in range(N):
        if i != start:
            tot += bfs(start, i)
    return tot

# start 을 넣어주는것
for i in range(N):
    kevin.append(get_kevin(i))


# 인덱스랑 같이 받아오기
for i, v in enumerate(kevin):
    if ans[1] > v:
        ans(i, v)

print(ans[0] + 1)

