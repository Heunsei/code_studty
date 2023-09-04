# N개의 상자 모두 0
# Q회동안 범위의 상자들을 동일 숫자로 변경
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    # Q번동안 첫번째일 때 L R 범위의 숫자를 1로 설정
    LR = [list(map(int, input().split())) for _ in range(Q)]
    box = [0]*N
    # Q번동안 LR에 있는 좌표값을 [i][0] , [i][1]이렇게 접근해서 변경
    for q in range(Q):
        for i in range(LR[q][0]-1, LR[q][1]):
            box[i] = q+1

    result = ' '.join(map(str, box))
    print(f'#{tc} {result}')

