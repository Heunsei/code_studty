# NxN 배열안에 숫자 입력
# MxM 크기의 파리채로 후려침
def get_sum(n, m, ran):
    result = 0
    for i in range(n, n+ran):
        for j in range(m, m+ran):
            if 0<= i < N and 0 <= j < N:
                result += arr[i][j]
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [0, 1, 1]
    dj = [1, 1, 0]
    max_fly = 0
    # 탐색 시작 좌표로부터 i + M-1 만큼 j + M-1만큼 범위 탐색
    tmp = 0
    for i in range(N):
        for j in range(N):
            tmp = get_sum(i, j, M)
            if tmp > max_fly:
                max_fly= tmp

    print(f'#{tc} {max_fly}')