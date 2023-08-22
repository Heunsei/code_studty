# 이진 힙 만들기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 1  # tree의 시작점 그리고 우리가 넣은 원소의 마지막 인덱스값

    for i in range(N):
        if tree[i] == 0:
            tree[last] = arr[i]
        else:
            last += 1
            tree[last] = arr[i]
            child = last
            parent = child // 2

            while parent >= 1 and tree[parent] > tree[child]:
                tree[parent], tree[child] = tree[child], tree[parent]
                child = parent
                parent = child // 2

    print(tree)