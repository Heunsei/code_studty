# Linked List
- 다음을 지목하는 포인터를 가진 구조
- head 와 tail 을 가진 자료구조
- 끝에 삽입하는 append 와 삭제하는 pop()은 O(1)만큼 시간이 걸림
- n 번째 원소에 접근할때 O(n)만큼 시간이 걸림
- 맨처음 idx 에 삽입을 하거나 삭제를 할 때 O(1)만큼 시간이 걸림
- 중간에 삽입, 삭제 할때는 O(n)만큼 시간이 걸림
- list 에서는 특정 원소에 접근할 때 O(1) 만큼 시간이 걸리지만, LL에서는 O(n)만큼 걸림

- 구현
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # 4가지 함수는 전부 클래스를 생성해야함
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self, value):
        new_node = Node(value)       
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def get(self, index):
        if index < 0 or index >= self.length
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    def remove(self,index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    def print_list(self):
        temp = self.head
        while temp if not None:
            print(temp.value)
            temp = temp.next 
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):   
            after = temp.next
            temp.next = before
            before = temp
            temp = after

```