# 완전 이진 트리는 배열을 만들어서 배열 index 정점 접근으로 트리를 생성
def inorder(p, N):  # N은 완전 이진트리의 마지막 정점
    if p <= N:
        inorder(p*2, N)            # 왼쪽 자식으로 이동
        print(tree[p], end='')     # 출력 // 중위 순회
        inorder(p*2+1, N)          # 오른쪽 자식으로 이동


T = 10
for tc in range(1, T+1):
    N = int(input())
    # 완전 이진트리는 정점번호까지 전부 다 채워둠
    tree = [0] * (N+1)  # N번 노드까지 있는 완전 이진트리
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]
    # 중위 순회
    print(f'#{tc}', end=' ')
    inorder(1, N)  # root = 1
    print()