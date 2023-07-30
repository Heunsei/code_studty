# 괄호 ()
# 이게ㅐ먼말이지 ㅇ;
# 와 풀었다

def check_str_end(get_string,end_num):
    if get_string[0] == ')':
        print('NO')
        return False
    
    if get_string[end_num] == '(' : 
        print('NO')
        return False
    
def compare(get_string):
    # '(' 입력시 오픈한거니까 닫을게 필요함
    # 닫는걸 opener를 줄이는걸로 표현
    opener = 0
    for n in range(len(get_string)):
        if get_string[n] == '(':
            opener += 1
        else :
            opener -= 1
        if opener < 0:
            print("NO")
            return
    if opener == 0:
        print("YES")
    else :
        print("NO")
    
test_case = int(input())

for num in range(test_case):
    
    get_string = list(input())
    #print(get_string)
    
    end_num = len(get_string)
    
    # 일단 ) 로 시작하면 no
    if check_str_end(get_string,end_num-1) == False :
        continue
    
    compare(get_string)