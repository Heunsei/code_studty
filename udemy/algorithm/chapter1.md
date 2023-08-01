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

# Vector 동적배열같은 느낌

# 연결리스트
- 삽입 삭제가 빠름 O(n)
- 탐색이 느림 > N번째 리스트에 접근하려면 n만큼 이동해야함
- 값을 저장할 노드와 다음 노드의 주소를 가진 노드 두개가있음

# Stack - 후입선출 구조
- 맨위 의 값 > head or top으로 표현 

# Queue - 선입선출
- std::queue
- form collentions import deque
- Queue모듈이 있긴한데 느려서 잘안쓰고 deque씀 (python)
- q.push(dataa) , q.append(data)
- q.pop() <- 맨 앞요소 삭제, q.popleft()
