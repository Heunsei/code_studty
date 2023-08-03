# 소인수분해
T = int(input())
for tc in range(1,T+1):
    test_case = int(input())
    result = [0] * 5
    #print(result)
    #print(test_case)
    while 2 <= test_case:
        if test_case % 11 == 0:
            test_case //= 11
            result[4] +=1
        
        elif test_case % 7 == 0:
            test_case //= 7
            result[3] +=1
        elif test_case % 5 == 0:
            test_case //= 5
            result[2] +=1
            
        elif test_case % 3 == 0:
            test_case //= 3
            result[1] +=1
            
        elif test_case % 2 == 0:
            test_case //= 2
            result[0] +=1
    
    res = ' '.join(map(str, result))
    print(f'#{tc} {res}')