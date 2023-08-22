def preorder(node):
    if node == 0:
        return
    print(node, end=' ')
    # preorder(left[node])
    # preorder(right[node])
    preorder(tree[node][0])
    preorder(tree[node][1])

# LVR
def inorder(node):
    if node == 0:
        return
    inorder(left[node])
    print(node, end=' ')
    inorder(right[node])

# LRV
def postorder(node):
    if node == 0:
        return
    postorder(left[node])
    postorder(right[node])
    print(node, end=' ')



V = int(input())  # 노드의 개수
E = V - 1  # 간선의 개수
edge = list(map(int, input().split()))

# 왼쪽 자식
left = [0] * (V + 1)
# 오른쪽 자식
right = [0] * (V + 1)
parent = [0] * (V + 1)

# 왼쪽, 오른쪽, 부모
tree = [[0] * 3 for _ in range(V+1)]
print(tree)

# 간선 정보를 전수 조사
# 간선 정보가 정렬되어 있지 않다면 정렬하고 넣는게 좋다
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:  # 왼쪽 자식이 기록 x
        left[p] = c
    else:
        right[p] = c

    parent[c] = p  # 부모 리스트에 저장

    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p

root = 0
for i in range(1, V+1):
    if parent[i] == 0:
        root = i
        break

print(left)
print(right)
print(parent)

print('------전위순회------')
preorder(root)
print('------중위순회------')
inorder(root)
print('------후위순회------')
postorder(root)