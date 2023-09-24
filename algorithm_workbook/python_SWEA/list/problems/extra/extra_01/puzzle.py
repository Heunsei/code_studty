T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 길이가 N인 2중리스트 설정
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 흰부분은 1 검은부분은 0
    # 흰부분에 길이가 K인 단어가 들어갈 수 있는지 판단

    # 한 열씩, 한 행씩만 검색할 것
    # count중 검은색을 만나면 몇칸인지 확인 후 다음꺼 확인

    # 행만 순회하면서 k를 늘려

    print('case I')
    res_i = 0
    for i in range(N):
        for j in range(N):
            if j == 0:
                count = 0
                for k in range(N):
                    if puzzle[i][j+k] == 1:
                        count += 1
                    if count > 0 and puzzle[i][j+k] == 0:
                        if count == K:
                            res_i += 1
                            count = 0
                        else:
                            count = 0
                #print('count : ', count)
                if count == K:
                    res_i += 1
    #print(res_i)
    #print('case J')
    res_j = 0
    for j in range(N):
        for i in range(N):
            if i == 0:
                count = 0
                for k in range(N):
                    if puzzle[i+k][j] == 1:
                        count += 1
                    if count > 0 and puzzle[i+k][j] == 0:
                        if count == K:
                            res_j += 1
                            count = 0
                        else:
                            count = 0
                #print('count : ', count)
                if count == K:
                    res_j += 1
    #print(res_j)
    print(f'#{tc} {res_i + res_j}')
