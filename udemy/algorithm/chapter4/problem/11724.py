=# 방향이 없는 그래프
import pprint
import sys
sys.setrecursionlimit((10 ** 6))
input = sys.stdin.readline
N, M = map(int, input().split())
# 간선 갯수가 N(N-1)/2 만큼
# > nC2 n개의 정점중에 두개 고르기 (인접행렬)
# 조건에 범위가 1 <= u,v <=N
# 양방향이니까 행렬을 사용..?

adj = [[0] * N for _ in range(N)]

for _ in range(M):
    # 조건 때문에 1빼면서 시작
    a, b = map(lambda x: x - 1, map(int, input().split()))
    # 양방향 이니까 대칭으로
    adj[a][b] = adj[b][a] = 1
# i번째 정점과 연결된 점들
pprint.pprint(adj)
chk = [False] * N
# 연결개수
ans = 0
def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            # 체크를 먼저하기
            chk[nxt] = True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)
    