# 비트연산자로 부분집합 만들어서 조건까지
T = int(input())
for tc in range(1,T+1):
    case = list(map(int, input().split()))
    
    case_len = 0
    
    for i in case:
        case_len += 1
        
    result = 0
    is_there = 0
    for i in range(1 << case_len):
        tmp = []
        sum_of_case = 0
        for j in range(case_len):
            if i & (1 << j):
                tmp.append(case[j])
        print(tmp)        
        for t in tmp:
            sum_of_case += t
        if len(tmp) == 0:
            continue
        if sum_of_case == 0:
            result += 1
        
        if result > 0:
            is_there = 1
    
    print(f'#{tc} {is_there}')    
    