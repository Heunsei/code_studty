# 행렬을 회전 시키기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1 2 3
    # 4 5 6
    # 7 8 9
    
    # 출력마다 회전시킨 케이스들을 한줄씩 출력
    case1 = []
    for j in range(N):
        tmp = []
        for i in range(N-1, -1, -1):
            tmp.append(arr[i][j])
        case1.append(tmp)
    #print(case1)
    case2 = []
    for i in range(N-1, -1, -1):
        tmp = []
        for j in range(N-1, -1, -1):
            tmp.append(arr[i][j])
        case2.append(tmp)
    #print(case2)

    case3 = []
    for j in range(N-1, -1, -1):
        tmp = []
        for i in range(N):
            tmp.append(arr[i][j])
        case3.append(tmp)
    #print(case3)

    print(f'#{tc}')
    for i in range(N):
        cs1 = ''.join(map(str, case1[i]))
        cs2 = ''.join(map(str, case2[i]))
        cs3 = ''.join(map(str, case3[i]))
        print(f'{cs1} {cs2} {cs3}')




