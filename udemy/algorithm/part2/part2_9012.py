# 한번 풀었던문제 스택으로 다시 접근
# 괄호
for _ in range(int(input())):
    stk = []
    isVPS = True
    for ch in input():
        # 입력받을때 (만 받고 ) 받으면 지우기
        if ch == '(':
            stk.append(ch)
        else:
            # 지울때 길이가 1보다 길면 팝
            if len(stk) > 0:
                stk.pop()
            # 지울때 0이면 쌍을 이룰애가 없으니
            # 볼것도 없이 false
            else:
                isVPS = False
                break

    if len(stk) > 0:
        isVPS = False
    # VPS가 true면 YES 아니면 NO
    print('YES' if isVPS else 'NO')
