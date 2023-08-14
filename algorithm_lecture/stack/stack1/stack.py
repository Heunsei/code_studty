# stack class 직접 구현
class Stack:
    # 스택의 크기
    # size를 받아옴
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.top = -1  # 없다는 뜻

    def pop(self):
        if self.isEmpty():
            raise Exception('스택에 값이 없습니다')
        else:
            value = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return value

    def push(self, item):
        if self.isFull():
            raise Exception('스택이 가득 차 있습니다')
        else:
            self.top += 1
            self.items[self.top] = item

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty():
           raise Exception('스택에 값이 없습니다')
        else:
            return self.items[self.top]

# 3짜리 스택 생성
s1 = Stack(3)

print(s1.items)
print(s1.top)
#print(s1.peek())
print(s1.push('A'))
print(s1.items)
print(s1.top)
s1.pop()
print(s1.items)