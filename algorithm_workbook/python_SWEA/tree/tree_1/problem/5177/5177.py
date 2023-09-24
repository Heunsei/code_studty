# 이진 힙

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N + 1)
    # 트리의 마지막 인덱스를 나타냄
    last = 1
    for i in range(N):
        # 1번째 값이 0이면
        if tree[i] == 0:
            tree[last] = arr[i]
        else:
            # 그게 아니면 마지막 값을 관리할 인덱스를 하나 올려주고 
            # arr의 값을 tree에 넣어줌
            last += 1
            tree[last] = arr[i]
            # 현재 값을 자식노드로 설정
            child = last
            # 그 부모값의 인덱스를 설정
            parent = child // 2
            # 1번 인덱스까지 child값이 더 작으면 바꿔줌
            # 내림차순으로 바꾸려면 부등호만 바꿔주면 됨
            while parent >= 1 and tree[parent] > tree[child]:
                tree[parent], tree[child] = tree[child], tree[parent]
                # 위치를 바꿔줬으니 인덱스를 다시 초기화
                child = parent
                parent = child //2
    ans = 0
    last_node = N // 2
    print(tree)
    while last_node != 0:
        ans += tree[last_node]
        last_node //= 2

    print(f'#{tc} {ans}')
