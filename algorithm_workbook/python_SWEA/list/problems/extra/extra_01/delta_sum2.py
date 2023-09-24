# 풍선 2
# 입력받은 값에 들어있는 값만큼 더 나가서 탐색

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    mk_list = [list(map(int, input().split())) for _ in range(N)]
    print(mk_list)

    max_val = 0
    repeat = 0

    for i in range(N):
        for j in range(M):
            # 시작좌표, count를 더하면서 시작
            count = mk_list[i][j]
            for k in range(4):
                # 방향만큼 몇번 더 갈지 조정하는 반복문
                for p in range(1, mk_list[i][j]+1):
                    ni, nj = i + di[k] * p, j + dj[k] * p
                    if 0 <= ni < N and 0 <= nj < M:
                        count += mk_list[ni][nj]
            if max_val < count:
                max_val = count

    print(f'#{tc} {max_val}')
