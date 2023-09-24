# 계산기
for tc in range(1, 11):
    cal_len = int(input())
    cal = input()
    stack = []
    result = ''
    for char in cal:
        # 연산자면 검사 후 stack에 append
        if char in "+*":
            # '*' -> * 또는 /를 만날때까지( 자신과 동등한 연산자를 만날때 까지)
            if char == '*':
                while stack and stack[-1] in '*':
                    # result 에 스택에 있는것 팝하고
                     result += stack.pop()
                    #자기 자신은 stack에 넣는다
                stack.append(char)
            elif char == '+':
                # +는 스택에 있는걸 전부 넣고
                while stack : #and stack[-1] in '+':
                     result += stack.pop()
                # 자기자신을 빈 스택에 넣어준다
                stack.append(char)
        # 숫자면 result 에 넣어주기
        else:
            result += char
    while stack:
        result += stack.pop()
    # result 를 계산할 스택2
    stack2 = []
    for char in result:
        if char not in '+*':
            stack2.append(char)
        else:
            # 스택에 있는건 연산자 또는 피연산자 피연산자는 str 형이라 int로 변환
            if char in '+':
                a = int(stack2.pop())
                b = int(stack2.pop())
                stack2.append(a+b)
            elif char in '*':
                a = int(stack2.pop())
                b = int(stack2.pop())
                stack2.append(a * b)
    # 스택에 0번째를 출력
    # 스택에 2 이상의 원소가 있다면 잘못 계산된것
    print(f'#{tc} {stack2[0]}')
