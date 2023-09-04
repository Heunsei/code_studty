import sys
sys.stdin = open('input_2.txt')


def search():
    if char == ')':
        tmp = 0
        # stack에 값이 있는 동안
        while stack:
            val = stack.pop()
            # val 정수일떄
            if val.isdigit():
                # 값 누적
                tmp += int(val)
            # val '(' 일떄
            elif val == '(':
                # 누적된 값을 stack에 추가
                stack.append(str(tmp))
                return True
            # val '{' 일떄
            elif val == '{':
                # 조사 멈춤
                # 이제.. 더 조사 할 필요 없어요...
                print(stack, tc)
                check = False
                return False
        else:
            return False
    elif char == '}':
        tmp = 1
        # stack에 값이 있는 동안
        while stack:
            val = stack.pop()
            # val 정수일떄
            if val.isdigit():
                # 값 누적
                tmp *= int(val)
            # val '{' 일떄
            elif val == '{':
                # 누적된 값을 stack에 추가
                stack.append(str(tmp))
                return True
            # val '(' 일떄
            elif val == '(':
                # 조사 멈춤
                # 이제.. 더 조사 할 필요 없어요...
                check = False
                return False
        else:
            return False

T = int(input())

for tc in range(1, T+1):
    word = input()
    # stack
    stack = []
    # 모든 글자에 대해서 다 조사
    for char in word:
        # 혹시... 계속 조사해도 되요?
        # check = True

        # stack에 넣을 값은 )} 빼고 전부다
        # if char != ')' and char != '}':
        #     stack.append(char)
        if char not in ')}':
            stack.append(char)
        else:
            result = search()
            if result == False:
                break

        # 혹시 우리 다음 단어 조사 안해도 되요?
        # if check == False:
        #     break

    if len(stack) >= 2 or not stack:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {stack[-1]}')
