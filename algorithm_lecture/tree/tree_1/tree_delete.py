# 힙에서 삭제 구현
def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1  # 루트에 옮긴 값을 자식과 비교
    c = p * 2  # 왼쪽 자식 (비교할 노드번호)
    while c <= last:        # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c + 1]:  # 오른쪽이 있고, 걔가 더크면
            c += 1      # 비교대상이 오른쪽 노드로 변경
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c   # 자식을 새로운 부모로
            c = p * 2   # 왼쪽 자식 번호를 계산
    return tmp


# 힙 생성
heap = [0] * 100
last = 0  # 마지막 정점 번호

