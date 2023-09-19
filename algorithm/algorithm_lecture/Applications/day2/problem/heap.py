# 최소 힙 구현
# 전체 데이터 수
N = 4
# 삽입 해야할 값
data = [10, 15, 100, 1]

# 트리 , 0번 노드는 안쓸거임
heap = [0] * (N+1) 
# 트리에 삽입할 노드 번호
last = 1

# 데이터 전부 삽입
for i in range(N):
    heap[last] = data[i]
    # 새로 추가된 값을 자식으로 보고
    child = last
    # 부모 위치 초기화
    parent = child // 2
    # 부모가 있을 때 까지 반복
    # 부등호 바꾸면 최대 힙
    while parent >= 1 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2
    print(heap, data[i])
    # 부모가 가진 값이 내가 가진값보다 작아야 함
    last += 1

print(heap)