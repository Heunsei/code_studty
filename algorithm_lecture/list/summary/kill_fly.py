# test case
T = int(input())
for tc in range(1, T+1):
    # NxN arr, MxM 파리채
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max = 0

    for i in range(N-M):
        for j in range(N-M):
            tmp = 0
            for a in range(i, i+M):
                for b in range(j, j + M):
                    tmp += arr[a][b]
            if tmp > max:
                max = tmp
    print(max)