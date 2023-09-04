import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 노드의 개수, 리프노드의 개수, 값을 출력할 노드
    N, M, L = map(int, input().split())
    # 리프노드의 번호와 자연수
    tree = [0] * (N+1)  # tree의 개수는 노드의 개수 + 1
    for i in range(M):
        node, val = map(int, input().split())
        tree[node] = val
    print(tree)
    # 어차피 리프노드들 밖에 없으니까 서로 더해서 올려주자
    # 역으로 올라가서 부모 인덱스에 값을 누적
    for idx in range(N, 1, -1):
        parent = idx // 2
        tree[parent] += tree[idx]
    ans = tree[L]
    print(f'#{tc} {ans}')