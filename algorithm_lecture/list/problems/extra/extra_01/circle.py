T = int(input())
for tc in range(1,T+1):
    N = int(input())
    count = 0
    for i in range(-N,N+1):
        for j in range(-N, N+1):
            if i**2 + j**2 <= N**2:
                count+=1
    print(f'#{tc} {count}')