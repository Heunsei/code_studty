# 행렬 덧셈
N, M = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

tmp = [[0]*M for _ in range(N)]
fir = 0
for i in range(N):
    for j in range(M):
        tmp[i][j] = A[i][j] + B[i][j]

for i in tmp:
    a = ' '.join(list(map(str, i)))
    print(a)