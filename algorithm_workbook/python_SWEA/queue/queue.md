### Queue
1. 선형 자료구조
2. 삽입 삭제의 위치가 제한적임
3. 선입 선출 구조

### 기본 연산
1. 삽입 enQueue
2. 삭제 deQueue
3. 생성 createQueue()
4. 확인 isEmpty() isFull()
5. 삭제없이 반환 Qpeek()

### BFS 조건을 만족했을 때 탐색하는거 ㅇㅇ



```python
def BFS(G, v): # 그래프, 시작점
    visited = [0] * v + 1
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t] :
            visited[t] = True
            visit(t)
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)
```