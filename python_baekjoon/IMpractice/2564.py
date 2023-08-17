# 직사각형을 돌면서 길이의 최소값을 찾기
# 가로 세로
M, N = map(int, input().split())
# 상점의 수
T = input()
arr = []
for _ in range(T):
    # 1 : 북쪽, 2 : 남쪽, 3 : 서쪽, 4 : 북쪽
    dir, pos = map(int, input().split())
    arr.append([dir, pos])
