N = int(input())
di = [0,1,0,-1] # 오른쪽 아래 왼쪽 위
dj = [1,0,-1,0]
# N번만큼 받아오겠다.
arr = [list(map(int,input().split())) for _ in range(N)]

max_v = 0 
for i in range(N): # i, j에 대해
    for j in range(N):
        s = arr[i][j]
        for k in range(4):
            ni, nj = i+di(k), j+dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                s += arr[ni][nj]
        # 주변원소 합
        if max_v < s:
            max_v = s