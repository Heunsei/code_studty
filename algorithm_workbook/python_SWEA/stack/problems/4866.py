# 괄호검사
T = int(input())
for tc in range(1, T+1):
    
    tmp = []      # 우리가 고려해야할 특수문자만 받아오기
    result = []   # 받아온 특수문자들을 검사할 리스트
    for i in input():
        if i == '\'':
            tmp.append(i)
        if i == '(' or i == ')' or i == '{' or i == '}':
            tmp.append(i)
            
    del_len = []
    # 작은 따옴표를 기준으로 무시할 범위를 찾음
    # tmp리스트 안의 ' '로 싸인 부분을 전부 자름
    for i in range(len(tmp)):
        if tmp[i] == '\'':
            del_len.append(i) (('{{}'))
    if len(del_len) >= 2:
        del tmp[del_len[0]: del_len[1]+1]
        
    # tmp에 남아있는 특수문자만 받아온다 라고 설정하고
    # result에 하나하나 넣어보면서 검사
    for i in tmp:
        if len(result) == 0:
            result.append(i)
        # 무언가 있다
        else :
            # ) 바로 이전에 ( 가 존재한다면 
            # 마지막을 pop
            if i == ')' and result[-1] == '(':
                result.pop()
            elif i == '}' and result[-1] == '{':
                result.pop()
            # 그게아니면 result에 그냥 넣어줌
            else:
                result.append(i)
    # result 가 비어있다면 짝이 모두 맞는거니 통과
    # 그게 아니라면 짝이 맞지 않는것이니 0출력
    if len(result) == 0:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')



