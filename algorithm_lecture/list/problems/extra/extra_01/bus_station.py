T = int(input())
for tc in range(1,T+1):
    N = int(input())
    station = [0] * 5000
    # station을 미리 설정하고
    for i in range(N):
        # 받아오는 1~3이란범위를 바로
        n, m = list(map(int,input().split()))
        # station 에 넣어주기
        # 1번째는 idx 0에 해당
        for j in range(n-1,m):
            station[j] +=1
    P = int(input())
    check_list = [int(input()) for _ in range(P)]
    result = []
    
    for i in check_list:
        result.append(station[i-1])
    
    res = ' '.join(map(str, result))
    print(f'#{tc} {res}')