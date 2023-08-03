#풍선 터뜨리기
T = int(input())
for tc in range(1,T+1):
    M, N = list(map(int,input().split()))
    result = []
    for i in range(M):
        row = list(map(int,input().split()))
        result.append(row)
              
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    
    max_sum = 0
    for i in range(M):
        for j in range(N):
            tmp = result[i][j]
            for k in range(4):
                ni = i + di[k]               
                nj = j + dj[k]               
                if 0 <= ni < M and 0 <= nj < N:
                   tmp += result[ni][nj]
            if max_sum < tmp:
                max_sum = tmp
    print(f'#{tc} {max_sum}') 
    
    