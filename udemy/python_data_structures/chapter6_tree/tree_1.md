### 트리
- 노드를 사용해서 이진트리 생성
- 아래에 left 와 right 그리고 value 를 가지는 자료구조
- 다른 노드를 지정해서 사용가능
- 꼭 이진트리일 필요는 없지만 여기서는 이진으로 생성
- BST (이진탐색트리) 의 탐색 시간은 O(logN)

# 구현
- 노
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    # 생성시에는 아무것도 넣지 않음
    def __init__(self):
        self.root = None
    # 추가하려는 값이 이미 있을때
    # root 가 비어 있을때
    # 좌/우를 비교하고 삽입
    def insert(self, value):
        new_node = Node(value)
        if  self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node == temp:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is Nonw:
                    temp.right = new_node
                    return True
                temp = temp.right
          

```