N = 6
arr = [6, 3, 2, 7, 9, 1]

# 부모노드는 안쓸거니까
tree = [0] * (N+1)
last = 1
for i in range(N):
    if tree[i] == 0:
        tree[last] = arr[i]
    else:
        last += 1
        tree[last] = arr[i]
        child = last    # 자식의 위치
        # 완전 이진 트리에서 부모의 위치
        parent = child // 2
        print(tree)

        while parent >= 1 and tree[parent] > tree[child]:
            # 부모, 자식의 값 교환
            tree[parent], tree[child] = tree[child], tree[parent]
            # 부모 자식 위치를 바꿧으니 자식의 위치 설정
            child = parent
            parent = child // 2
        print(tree)

print(tree)
