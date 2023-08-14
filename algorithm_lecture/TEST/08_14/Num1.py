# 테스트케이스
T = int(input())
for tc in range(1, T + 1):
    # 격자의 크기
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 검색을 위한 좌표
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    #봉우리의 수
    cnt = 0

    for i in range(N):
        for j in range(N):
            check = arr[i][j]
            # 일단 True로 놓고
            is_top = True
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    # 옆에있는 것중 하나라도 같거나 크면 False로
                    if arr[ni][nj] >= arr[i][j]:
                        is_top = False
            if is_top:
                cnt += 1

    print(f'#{tc} {cnt}')
