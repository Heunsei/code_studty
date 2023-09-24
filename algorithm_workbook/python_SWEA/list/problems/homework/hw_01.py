# 빌딩
# T > 빌딩의 개수
for num in range(10):    
    T = int(input())
    tc = list(map(int,input().split()))
    result = 0
    for i in range(2,T-2):
        tmp_list = []
        max = -1
        tmp_list.append(tc[i-2])
        tmp_list.append(tc[i-1])
        tmp_list.append(tc[i+1])
        tmp_list.append(tc[i+2])
        for tmp in tmp_list:
            if tmp > max:
                max = tmp
        if max < tc[i]:
            a = tc[i] - max
            result += a 
    print(f'#{num+1} {result}')
    
        
        