from pprint import pprint
# 배열을 입력받고 그것을 순회하면서 순서를 기록
# 오른쪽, 아래, 왼쪽, 위 방향으로 움직일것
# NxN 배열부터 시작 - cheack > ( x )
# 델타탐색을 위한 좌표 먼저 설정
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
snail = [[0]*T for _ in range(T)] # T번만큼 빈 배열 생성

#초기 좌표 설정
count = 1
i, j = 0, 0
# 방향을 바꿔줄 변수
dir = 0
snail[i][j] = count
while count < T**2:
    ni = i + di[dir]
    nj = j + dj[dir]
    if 0 <= ni < T and 0 <= nj < T and snail[ni][nj] == 0:
        count += 1
        snail[ni][nj] = count
        i = ni # 다음으로 갈 i 좌표
        j = nj # 다음으로 갈 j 좌표
    else :
        dir += 1
        if dir >= 4:
            dir = 0

for i in snail:
    pprint(i)