# 가장 첫줄에 테스트케이스 T
T = int(input())
for tc in range(1, T+1):
    repeat = int(input())
    # 빈 리스트 생성
    # 받는 정보들을 [문자, 출력횟수]로 묶어서 관리
    tmp = []
    for t in range(repeat):
        ins = list(input().split())
        tmp.append(ins)
    #print(tmp)
    count = 0
    print(f'#{tc}')
    # 이중 리스트를 순회하면서 출력값과 출력횟수를 받아옴
    # tmp[i][j] j = 0 에는 출력문자
    # tmp[i][j] j = 1 에는 출력횟수
    # 다만 입력값을 int 로 변환하면서 입력받은게 아니라
    # range 에 값횟수를 넣을때 int 형식으로 변환 필요
    for i in range(repeat):
        for j in range(int(tmp[i][1])):
            print(tmp[i][0], end='')
            count += 1
            if count == 10:
                print('')
                count = 0
    print()
