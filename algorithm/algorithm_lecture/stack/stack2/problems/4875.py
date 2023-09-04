from collections import deque
# 테스트케이스


def isValid(position_i, position_j):
    return 0 <= position_i < N and 0 <= position_j < N


def BFS(start_i, start_j):
    chk = [[False] * N for _ in range(N)]
    chk[start_i][start_j] = True
    dq = deque()
    dq.append((start_i, start_j))
    while dq:
        i, j = dq.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if isValid(ni, nj) and arr[ni][nj] != '1' and not chk[ni][nj]:
                chk[ni][nj] = True
                if arr[ni][nj] == "3":
                    print(f'#{tc} 1')
                    return
                dq.append((ni, nj))
    print(f'#{tc} 0')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    di = (0, 1, 0, -1)
    dj = (1, 0, -1, 0)

    # 시작 좌표 구하기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start_i = i
                start_j = j

    BFS(start_i, start_j)
