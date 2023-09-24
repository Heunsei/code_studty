T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 몇줄 받아올지
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        r_sum = 0
        for j in range(M):
            if arr[i][j] == 1:
                r_sum += 1
                # 끝에 닿으면
                if j == M - 1:
                    if result < r_sum:
                        result = r_sum
            else:
                if result < r_sum:
                    result = r_sum
                r_sum = 0

    for j in range(M):
        s_sum = 0
        for i in range(N):
            if arr[i][j] == 1:
                s_sum += 1
                # 끝에 닿으면
                if i == N - 1:
                    if result < s_sum:
                        result = s_sum
            else:
                if result < s_sum:
                    result = s_sum
                s_sum = 0

    print(f'#{tc} {result}')
