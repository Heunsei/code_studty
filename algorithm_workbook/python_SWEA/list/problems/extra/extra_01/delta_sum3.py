T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_val = 0

    for i in range(N):
        for j in range(M):
            count = arr[i][j]
            # 방향을 고정
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 고정된 방향에서 이동. di dj를 곱하는 식으로 
                # (어차피 1이니까) 추가적으로 이동
                # 첫 시행은 0 이니까 추가할 이동거리가 없는거
                # 두 번째 시행에 di에 1이 들어가니 기존 i,j에서 2만큼 이동한거
                # ni는 이미 한칸 이동한것, 그거에 추가이동
                for p in range(arr[i][j]):
                    ni, nj = ni+di[k]*p, nj+dj[k]*p
                    if 0 <= ni < N and 0 <= nj < M:
                        count += arr[ni][nj]
            if max_val < count:
                max_val = count
    print(f'#{tc} {max_val}')

