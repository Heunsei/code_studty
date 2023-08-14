T = int(input())
for tc in range(1, 1 + T):
    # 리스트에 하나하나 넣어서 관리
    arr = list(input())
    #print(arr)

    # 괄호 검사를 할 스택
    check_stack = []
    # 계산할 스택 / 계산결과
    cal_stack = []
    result_stack = []
    numbers = []
    result = 0
    for i in arr:
        if i == '(' or i == '{':
            check_stack.append(i)
        if check_stack:
            if i == ')' and check_stack[-1] == '(':
                check_stack.pop()
            elif i == ')' and check_stack[-1] != '(':
                check_stack.append(i)
            if i == '}' and check_stack[-1] == '{':
                check_stack.pop()
            elif i == '}' and check_stack[-1] != '{':
                check_stack.append(i)

    # 괄호 안맞으면 얄짤없이 -1 출력
    if len(check_stack):
        print(f"#{tc} -1")
        continue

    if arr[0] == ')' or arr[0] == '}':
        print(f"#{tc} -1")
        continue

    if arr[0] == '(' or arr[0] == '{':
        for i in arr:
            cal_stack.append(i)
    # 괄호 통과해도 시작이 괄호가 아니면 -1 출력
    else:
        print(f"#{tc} -1")
        continue

    for i in cal_stack:
        #print(result)
        if i == '(' or i == '{':
            result_stack.append(i)
        elif i != ')' and i != '}':
            result_stack.append(int(i))

        if i == ')' and result_stack:
            if result_stack[-1] == '(':
                result_stack.pop()
            elif result_stack[-1] != '(':
                result += result_stack.pop()
        if i == '}'and result_stack:
            if result_stack[-1] == '{':
                result_stack.pop()
            elif result_stack[-1] != '(':
                result *= result_stack.pop()
        # if i != '(' and i != ')' and i != '{' and i != '}':
        #     if result_stack[-1] == '(':
        #         #result += int(i)
        #     elif result_stack[-1] == '{':
        #         #result *= int(i)

    print(f'#{tc} {result}')