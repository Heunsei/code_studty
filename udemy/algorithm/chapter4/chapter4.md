# DFS, BFS, 백트래킹
### graph
- 포인트와 포인트를 이어주는 역할
- Vertex(Node) 정점이 몇개~ vertex를 잇는 edge
- 무방향 그래프
- 방향 그래프
- 순환 그래프
- 비순환 그래프

### 그래프를 코드로 나타내는 법
- 라이브러리에서 따로 제공해주는게 없으니 만들어야함
1. 인접행렬
- 간선 정보를 행렬에 담아서 관리
- 행은 간선의 시작 idx 열은 도착 idx
- 무방향 그래프는 행열을 대칭으로 채워줌
- 간선 하나가 두개의 방향을 나타내기때문
2. 인접리스트(링크드리스트)
- C++에서는 백터 / python 은 리스트로
3. 인접행렬이 인접리스트보다 자리를 많이 차지함
- 인접행렬은 N^2만큼 공간이 필요.
- 임의 접근을통해 빠르게 edge 의 유무를 판단가능  
- 인접 리스트에는 임의접근을 쓰지도 못하고
- 모든값을 돌면서 특정 edge 가 있는지 확인(O(N))
- edge가 적을수록 인접리스트를 사용

### DFS (깊이 우선 탐색), 완전탐색임
- 트리에서 맨 왼쪽아래부터 탐색 이런식
- 스택이나 재귀를 사용
```python
# 인접행렬
adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[2][4] = 1
adj[1][5] = 1
adj[5][6] = 1
# 현재 방문하는 노드의 번호를 인자로 받아옴
def dfs(now):
    # 다음 방문할 노드
    for nxt in range(13):
        # 현재 노드에서 다음으로 진행할 노드가 있다면 다음 노드를 호출
        if adj[now][nxt]:
            dfs(nxt)
    
dfs(0)
```
### BFS 너비 우선 탐색
- 큐를 이용해서 구현
- 큐를 만들고 탐색을 하려는 노드를 만들어줘야함
- 큐에 넣고 꺼내고의 반복
```python
from collections import deque
def bfs():
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)
```

## 인접행렬 인접리스트
- 인접행렬 O(N^2)
- 인접리스트 O(V+E)

# 델타탐색
- cpp
```cpp
const int di[4] = {0, 1, 0, -1};
const int dj[4] = {1, 0, -1, 0};
int N;
bool chk [100][100];    // 방문체크

bool isValidCoord(int i, int j){
    return 0 <= y && y < N && 0< = x && x < N;
    }
void dfs(int i, int j){
    chk[i][j] = true;
    for (int k = 0; k < 4 ; K++){
        int ni = di[k] + i;
        int nj = dj[k] + j;
    if(isValidCoord(ni, nj) && !chk[ni][nj]
        dfs(ni,nj);
    }
}
```

- python
```python
di = (0,1,0,-1)
dj = (1,0,-1,0)
chk = [[False] * 100 for _ in range(100)]

def is_valid_coord(i, j)
    return 0 <= i < N and 0 <= j < N

def bfs(start_i,start_j)
    q = deque()
    q.append((start_i, start_j))
    while len(q) > 0:
        i, j = q.popleft()
        chk[i][j] = True
        for k in ragne(4):
            ni = di[k] + i
            nj = dj[k] + j
            if is_valid_coor(ni,nj) and not chk[ni]nj]:
            q.append((ni,nj))
```

### 백트래킹
- 가능한 덜보겠다
- 가망성이 없으면 가지않는다
- DFS/BFS랑 방식은 유사하다

## 정리
- 공통점
1. 그래프 탐색 알고리즘
2. 완전 탐색 알고리즘(느림)
- 차이점
1. 탐색순서(BFS는 좌우, DFS는 맨 아래부터) 최단거리랑 관련

- 인접행렬
- edge 가 많으면 인접행렬 탐색이빠름
- 인접 리스트  
- edge 가 적은 그래프에 쓰는것이 좋음
- 메모리를 적게 먹는다