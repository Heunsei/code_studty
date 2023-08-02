N = int(input())
di = [0,1,0,-1] # 오른쪽 아래 왼쪽 위
dj = [1,0,-1,0]
# N번만큼 받아오겠다.
arr = [list(map(int,input().split())) for _ in range(N)]

max_v = 0 
for i in range(N): # i, j에 대해
    for j in range(N):
        s = arr[i][j]
        # 좌표를 기준으로 방향따라 m만큼 더하기
        # 이런식으로도 할수있다 인지필요
        for p in range(1,m):
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i+di*p, j+dj*p
                if 0 <= ni < N and 0 <= nj < N:
                    s +=arr[ni][nj]
            # 주변원소 합
            if max_v < s:
                max_v = s