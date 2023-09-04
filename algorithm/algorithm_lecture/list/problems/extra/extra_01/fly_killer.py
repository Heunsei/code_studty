#  파리는 언제죽을까?
T = int(input())
for tc in range(1, T+1):
    D, A, B, F = list(map(float, input().split()))
    time = D / (A+B)
    move = F * time
    print(f'#{tc} {move : .06f}')