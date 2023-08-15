# 계산기
for tc in range(1, 11):
    cal_len = int(input())
    cal = input()
    stack = []
    result = ''
    for char in cal:
        if char in "+*":
            if char == '*':
                while stack and stack[-1] in '*':
                     result += stack.pop()
                stack.append(char)
            elif char == '+':
                while stack : #and stack[-1] in '+':
                     result += stack.pop()
                stack.append(char)
        else:
            result += char
    while stack:
        result += stack.pop()
    # result를 계산할 스택2
    stack2 = []
    for char in result:
        if char not in '+*':
            stack2.append(char)
        else:
            if char in '+':
                a = int(stack2.pop())
                b = int(stack2.pop())
                stack2.append(a+b)
            elif char in '*':
                a = int(stack2.pop())
                b = int(stack2.pop())
                stack2.append(a * b)

    print(f'#{tc} {stack2[0]}')
