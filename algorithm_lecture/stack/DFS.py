# 노드와 간선의 갯수
# 노드번호를 받아서 그 노드부터 시작
def DFS(node):
    # 값을 넣어놓고 시작
    stack = [node]
    # 방문을 할수 있는지 없는지 체크할수있는 수단이 필요함
    visited = [False] * (V+1) # 노드가 7개인데 1부터시작하니까 1더해줌
    while stack: # 스택에 값이 있는 동안 탐색
        start = stack.pop()  # 항상 후입선출
        # 처음부터 끝까지 돌면서 갈수 있으면 다음조사를 할거임
        # 다음 위치가 조사한적이 있으면 안가도록 인덱스로 체크
        if visited[start] == 0:
            visited[start] = True
            print(start, end=' ')
            # 현재 위치 기준으로 다음 위치 조사
            # 0 부터 끝까지 노드조사
            for next in range(0, V+1):
                if adj[start][next] == 1 and visited[next] == 0:
    
V, E = map(int, input().split())
# 실제 간선 정보
data = list(map(int, input().split()))

#이동 가능정보
adj = [[0]*(V+1) for _ in range(V+1)]

# 간선을 순회
for i in range(0, E*2, 2):
    adj[data[i]][data[i+1]] = adj[data[i+1]][data[i]] = 1
