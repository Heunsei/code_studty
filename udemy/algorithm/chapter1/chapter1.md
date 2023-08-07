# 빠른 입출력 함수
```python
import sys
for _ in range(100000):
    n = int(sys.stdin.readline())
```
### arr
- 접근, 탐색이 빠름
- 중간에 삽입 시 배열의 뒷 요소를 전부 밀어야해서
속도가 느려짐
- arr + 2 x 4byte(int일때) = 메모리 주소값

### Vector 동적배열같은 느낌
- 자기혼자 크기를 조절가능

### 연결리스트
- 삽입 삭제가 빠름 O(n)
- 탐색이 느림 > N번째 리스트에 접근하려면 n만큼 이동해야함
- 값을 저장할 노드와 다음 노드의 주소를 가진 노드 두개가있음

### Stack - 후입선출 구조
- 맨위 의 값 > head or top 으로 표현 

### Queue - 선입선출
- cpp >>> std::queue
- python >>> form collections import deque
- Queue 모듈이 있긴한데 느려서 잘안쓰고 deque씀 (python)
- q.push(dataa) , q.append(data)
- q.pop() <- 맨 앞요소 삭제, q.popleft()

### Priority Queue (Heap)
- cpp > priority_queue<int> pq -max_heap  
- python > import heapq - min_heap
- queue 에 PriorityQueue 가 있긴함 threadSafe 해서 느림
- 그래서 heapq 사용
- 시간 복잡도는 주로 logN

```python
import heapq
pq = []
heapq.heappush(pq, 6)
heapq.heappush(pq, 12)
heapq.heappush(pq, 6)
print(pq)
while pq:
    print(pq[0]) # 최상단 노드의 값
    heapq.heappop(pq)
```

### map
- cpp map<string,int>m , key-val값으로 묶임, 레드블랙트리
- python m{} 딕셔너리 - 해시로 구성

```cpp
map<string,int> m;
m["Yoon"] = 40;
m["Heun"] = 100
printf("size : %d\n", m.size());
for(auto p : m)
    print("%d,%d\n", p.first(),p.second());
```

### Set 중복x 
```cpp
// insert 지원 삭제는 찾아봐야함
set<int> s;
s.insert(456);
s.insert(12);
s.insert(46);
s.insert(4652);
print("size : %d\n",s.size());
for(auto i : s)
    printf("%d\n", i);
```
- 파이썬에서 pop()을 하면 어떤값이 빠질지 모름 크게 쓰인다곤 하기힘듬.
- .remove()를 사용해서 주로 삭제