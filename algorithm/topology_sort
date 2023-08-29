# 위상정렬
- 순환하지 않는 방향 그래프에 대해서만 생성 가능
- 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면
여러가지 답이 존재한다.
- 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다
- 스택을 활용한 DFS를 이용해 위상 정렬을 수행 할 수 있다
```python
from collections import deque
# 노드의 개수와 간선의 개수를 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수를 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for i in range(v+1)]
__
# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A와 B를 이어줌
    # b에 대한 진입차수를 1증가
    indegree[b] += 1

def topology_sort():
    result = []  # 알고리즘 수행 결과를 담을 리스트
    q = deque()  # 큐 기능을 위한 덱 라이브러리
    
    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌때까지 반복
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for i in graph[now]:
        indegree[i] -= 1
        # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)
    # 출력
    for i in result:
        print(i, end=' ')
```