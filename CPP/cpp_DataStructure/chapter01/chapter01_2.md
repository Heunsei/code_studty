# 연속된 자료 구조와 연결된 자료 구조
## 6 반복자
- 임의 접근 반복자 : 특정 위치의 원소에 곧바로 접근 가능.
- 순방향 반복자 : 증가 연산만 가능하고, 첫 함수부터 움직여야함.
```cpp
advance() // 반복자와 거리 값을 인자로 받고, 반복자를 거리만큼 증가
next(); prev(); // 해당 반복자에서 지정 거리만큼 떨어진 반복자를 반환
```

## 7 std::list
- 이중연결 리스트 형태
```cpp
struct doubly_linked_list_node
{
  int data;
  doubly_linked_list_node* next;
  doubly_linked_list_node* prev;
}
```
- list에서는 원소 이동을 역방으로도 할 수 있으므로 원소 삽입을 위해 특정 원소 이전의 원소 반복자를 제공하지 않아도 됨,
대신, 정확하게 새로운 원소가 삽입될 위치를 가리키는 반복자를 함수 인자로 전달
- push_back(), emplace_back(), pop_back() 지원
-
### 7-1 반복자 무효화
- 반복자는 메모리 주소를 가르키는 포인터를 이용하여 구현되어 있기 때문에, 컨테이너가 변경될경우 제대로 작동 안할수도 있음.
- push_back()을 사용했을때, 경우에 따라 새 메모리를 할당하고 값을 복사하는데 그 경우 이전에 사용하던 포인터,참조가 모두 무효화 됨.

## 8 std::deque
### 8-1 deque의 구조
- push_front(), pop_front(), push_back(), pop_back() 모두 O(1)의 시간 복잡도로 작동
- 모든 원소에 대해 임의 접근 동작이 O(1)의 시간 복잡도로 동작
- 덱 중간에서 원소 삽입 또는 삭제는 O(n)의 시간 복잡도로 동작, 실제로는 최대 2/n 단계로 동작
- 양 방향으로 빠르게 확장할 수 있어야 하며, 모든 원소에 임의 접근제공
- 덱은 단일 메모리 청크가 아닌, 크기가 같은 여러개의 청크를 사용
- 덱의 맨 앞에 새로운 원소를 추가할때, 첫 번째 메모리 청크에 여유 공간이 없으면 새로운 청크를 할당하고, 그 메모리 청크 주소를, 덱의 첫번째 메모리 주소로 설정

```cpp
std::deque<int> deq = {1, 2, ,3 ,4, 5};
deq.push_front(0); >> {0, 1, 2, ,3 ,4, 5}
deq.push_back(6); >> {0, 1, 2, ,3 ,4, 5, 6}
```
## 9 컨테이너 어댑터
- std::stack > 데이터 처리와 보관을 위해 LIFO 후입선출 구조를 사용
- 스택은 컨테이너의 한쪽 끝에서만 데이터를 삽입하거나 삭제 할수 있으며, 한쪽 끝이 아닌곳에선 접근불가.
### 9-1 std::stack
- empty(), size(), top(), push(), emplace() 등 제공
- 스택은 기본적으로 vector가 아닌 deque 로 구현됨
- std::stack<int, std::list<int>> stk; 이런 식으로 선언 가능
### 9-2 std::queue
- stack과 다르게 FIFO 방식
- queue에서의 push는 push_back(), pop은 pop_front()을 의미
```cpp
std::queue<int> q;
q.push(1);
q.push(2);
q.push(3); >> {1,2,3}
q.pop(); >> {2,3}
```
### 9-3 priority_queue
- 우선순위 큐 / 원소 제거는 최소,최대 원소에 한해서 가능
- std::vector를 기본 컨테이너로 사용