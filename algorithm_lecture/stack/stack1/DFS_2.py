# 노드와 간선의 갯수
# 노드번호를 받아서 그 노드부터 시작
# 재귀 함수로
visited = [False] * (V + 1)  # 노드가 7개인데 1부터시작하니까 1더해줌
def DFS(node):
    visited[node] = True
    print(node, end=' ')
    for next in range(1, V + 1):
        if adj[node][next] == 1 and visited[next] == 0:
            DFS(next)

V, E = map(int, input().split())
# 실제 간선 정보
data = list(map(int, input().split()))

# 이동 가능정보
adj = [[0] * (V + 1) for _ in range(V + 1)]

# 간선을 순회
for i in range(0, E * 2, 2):
    adj[data[i]][data[i + 1]] = adj[data[i + 1]][data[i[]] = 1
