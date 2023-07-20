# 트리, 힙, 그래프
## 비선형 문제
- 선형 자료 구조로 표현불가능한 계층문제와 순환종속문제에 대한 해결법

## 트리 순회 방법
### 1. 전위 순회 (상위노드를 하위노드보다 먼저 방문한다)
- 현재 노드를 방문하고, 그다음은 현재 노드의 왼쪽 하위 노드를, 마지막으로 현재노드의 오른쪽 하위를 재귀적인 방식으로 방문
```cpp
static void preOrder(node* start)
{
  if(!start)
    return;
  std::cout << start->position << ", ";
  preOrder(start->first);
  preOrder(start->second);
}
```
### 2. 중위 순회
- 왼쪽 노드를 먼저 방문하고 현재노드를 그다음 오른쪽 노드를 방문
```cpp
static void inOrder(node* start)
{
  if(!start)
    return;
  inOrder(start->fisrt);
  std::cout << start->position << ", ";
  inOrder(start->second);
}
```
### 3. 후위 순회
- 두 자식 노드를 먼저 방문하고 현재노드 방문
```cpp
static void inOrder(node* start)
{
  if(!start)
    return;
  inOrder(start->fisrt);
  inOrder(start->second);
  std::cout << start->position << ", ";
}
```
### 4. 레벤 순서 순회
- 트리의 루트 노드부터 단계별로 차례대로 나열
```cpp
static void levelOrder(node* start)
{
  if(!start)
    return;
  std::queue<node*> q; // FIFO
  q.push(start);

  while(!q.empty())
  {
    int size = q.size();
    for(int i = 0; i < size; i++)
    {
      auto current = q.front();
      q.pop();

      std::cout<< current-> position <<", ";
      if(current->first)
        q.push(current->first);
      if(current->second)
        q.push(current->second);
    }
    std::cout << std::endl;
  }
}
```

## 이진 검색 트리(BFS)
- 부모 노드의 값 >= 왼쪽 자식 노드의 값
- 부모 노드의 값 <= 오른쪽 자식 노드의 값
- 삽입동작은 O(logN)의 복잡도를 가짐

