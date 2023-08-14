cal = '2+3*4/5'

result = ''

stack = []

for char in cal:
    if char in '+-*/()':
        print(char, '연산자')
        # 우선순위가 높은 순으로 조건문 처리
        if char == '(':
            stack.append(char)  # 우선순위가 가장 높으니까 push
        elif char in '*/':  # 마지막 값이 나와같은 */ 일때까지
            while stack and stack[-1] in '*/':
                result += stack.pop()
            stack.append(char)
        elif char in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
    else:
        result += char
    print(result, stack)
while stack:
    result += stack.pop()
print(result, stack)