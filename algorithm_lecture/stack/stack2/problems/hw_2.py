# 계산기 3
for tc in range(1, 11):
    N_len = int(input())
    N = input()
    stack = []
    result = ''
    for i in N:
        # 연산자 일 때
        if i in '()+*':
            if stack:
                if i == '+':
                    while stack and stack[-1] != '(':
                        result += stack.pop()
                    stack.append(i)
                elif i == '(':
                    stack.append(i)
                elif i == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()
                elif i == '*':
                    while stack and stack[-1] == '*':
                        result += stack.pop()
                    stack.append(i)
            # 스택이 비었으면 넣기
            else:
                stack.append(i)
        else:
            result += i
    while stack:
        result += stack.pop()
    stack2 = []
    for char in result:
        if char not in '+*':
            stack2.append(char)
        else:
            # 스택에 있는건 연산자 또는 피연산자 피연산자는 str 형이라 int로 변환
            if char in '+':
                a = int(stack2.pop())
                b = int(stack2.pop())
                stack2.append(a + b)
            elif char in '*':
                a = int(stack2.pop())
                b = int(stack2.pop())
                stack2.append(a * b)
    print(f'#{tc} {stack2[0]}')
