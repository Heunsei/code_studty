# 문자열의 처음과 끝에 접근

repeat = int(input())

for num in range(repeat):    
    get_string = list(input())
    offset = 0
    for num in get_string:
        offset+=1
    # 어차피 처음과 끝값이니 0을 넣어서 처음값 출력하고
    # offset으로 길이 측정했으니 마지막값만 넣어서 출력
    print(get_string[0]+get_string[offset-1])
