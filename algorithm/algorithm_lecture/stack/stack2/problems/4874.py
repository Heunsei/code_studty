T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    stack = []

    for char in arr:
        # 연산자일때
        if char in '+-*/':
            try:
                a = stack.pop()
                b = stack.pop()
            except IndexError:
                print(f'#{tc} error')
                break
            if char == '+':
                stack.append(int(a) + int(b))
            if char == '*':
                stack.append(int(a) * int(b))
            if char == '-':
                stack.append(int(b) - int(a))
            if char == '/':
                stack.append(int(int(b) / int(a)))
        elif char in '.':
            if len(stack) == 1:
                print(f'#{tc} {stack[0]}')
            else:
                print(f'#{tc} error')
        # 숫자일때 숫자를 넣어줌
        else:
            stack.append(char)
