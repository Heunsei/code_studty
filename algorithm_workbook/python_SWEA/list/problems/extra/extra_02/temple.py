
T = int(input())
for tc in range(1, T+1):
    # 배열을 받아와 그 배열의 열을 검사할 함수
    def row_serch(arr, N, M):
        result = 0
        for i in range(N):
            count = 0
            for j in range(M):
                if arr[i][j] == 1:
                    count += 1
                else:
                    if result < count:
                        result = count
                    count = 0
            # print('count', count)
            # print('result', result)
            if result < count:
                result = count
        return result


    def col_serch(arr, N, M):
        result = 0
        for j in range(M):
            count = 0
            for i in range(N):
                if arr[i][j] == 1:
                    count += 1
                if count >= 1 and arr[i][j] == 0:
                    if result < count:
                        result = count
                        count = 0
            # print('count', count)
            # print('result', result)
            if result < count:
                result = count
        return result
    # N x M
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    #print(row_serch(arr, N, M))
    #print(col_serch(arr, N, M))

    if row_serch(arr, N, M) > (col_serch(arr, N, M)):
        print(f'#{tc} {row_serch(arr, N, M)}')
    elif row_serch(arr, N, M) == (col_serch(arr, N, M)):
        print(f'#{tc} {row_serch(arr, N, M)}')
    else:
        print(f'#{tc} {col_serch(arr, N, M)}')
