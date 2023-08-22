# 이진 탐색 트리 구현
# 트리의 노드를 하나의 객체로 만들어서 다뤄보자
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

arr = [13, 2, 54, 12, 43, 23, 11, 43]

root = TreeNode(arr[0])

for val in range(1, len(arr)):
    insert(root, val)

print(root.value)
print(root.left.value)

inorder(root)