# 10x10 격자 색칠하기
# 케이스 몇번 시도해볼래
T = int(input())
for tc in range(1, T+1):
    # 몇번칠할래
    N = int(input())
    test_case = [list(map(int, input().split())) for _ in range(N)]
    # 색칠할 모눈종이
    arr = [[0] * 10 for _ in range(10)]

    count = 0
    for num in test_case:
        print(num)
        for i in range(num[0], num[2]+1):
            for j in range(num[1], num[3]+1):
                if arr[i][j] == 0:
                    arr[i][j] += num[4]
                elif arr[i][j] == 1 and num[4] == 2:
                    arr[i][j] += num[4]
                elif arr[i][j] == 2 and num[4] == 1:
                    arr[i][j] += num[4]

                if arr[i][j] >= 3:
                    count += 1

    print(f'#{tc} {count}')


