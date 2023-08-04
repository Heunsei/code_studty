import sys
sys.stdin = open('input.txt')

# 마지막 행에서 만난값이 2면 출발 좌표 출력
# 좌,우 우선 아래로 탐색
# 델타 탐색시 방향을 인덱스로 관리 할 수 있게 한다
di = [1, 0, 0]
dj = [0, -1, 1]

def serch(i, j):
    # 2찾으면 시작좌표 기록
    # 방문을 기록할 2차원 배열리스트
    visited = [[0]*100 for _ in range(100)]
    original_j = j
    # 방문표시
    visited[i][j] = 1
    while i != 99:
        for k in range(3):
            # 원본은 그대로니까 대입만 해두고
            ni = i + di[k]
            nj = j + dj[k]
            # 뒤에서 조건확인
            # if 0 <= ni < 100 and 0 <= nj < 100 and data[ni][nj]:
            if 0 <= ni < 100 and 0 <= nj < 100 and data[ni][nj] != 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                i, j = ni, nj

    # x == 99
    if data[i][j] == 2:
        return original_j
    else:
        return None


for _ in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        # 0번째 열의 i 행의 값이 1이면
        if data[0][i] == 1:
            result = serch(0, i)
        if result:
            break

    print(f'#{tc} {result}')


