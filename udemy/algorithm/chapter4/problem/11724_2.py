import sys
sys.setrecursionlimit((10 ** 6))
input = sys.stdin.readline

# 스스로 구현해보자
# 정점의 개수와 간선의 개수
N, M = map(int, input().split())
# 정점의 개수 N의 제곱만큼 인접행렬 생성
adj = [[0]*N for _ in range(N)]
chk = [False] * N
result = 0
# 연결된 두 정점
for _ in range(M):
# 1부터 받아오니까 (문제 안의 조거건)
# 넣을때 1 빼서 넣어주기
    a, b = map(int, input().split())
# 양방향 그래프니까 대각까지 1로 변경
    adj[a-1][b-1] = adj[b-1][a-1] = 1

def dfs(now):
# 정점의 개수만큼 검사
    for ntx in range(N):
        if adj[now][ntx] and not chk[ntx]:
            chk[ntx] = True
            dfs(ntx)

# 정점이 연결된 요소의 개수를 출력하니 정점의 개수만큼 검사해야함
for i in range(N):
    if not chk[i]:
        result += 1
        chk[i] = True
        dfs(i)

print(result)