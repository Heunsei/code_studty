# 레이저를 기준으로 파이프를 더하는것,,?
# 레이저가 열리면 이전에 있던 파이프를 더해줌
# 열리는 괄호면 일단 더하기
# 닫히는 괄호면 쇠막대의 끝 or 레이저의 끝
T = int(input())
for tc in range(1, 1+T):
    s = input()
    count = 0
    result = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            # 바로 전 요소가 ( 면 () > 레이저임
            if s[i-1] == '(':
                count -= 1
                result += count
            else:
                result += 1
                count -= 1
    print(f'#{tc} {result}')

            
