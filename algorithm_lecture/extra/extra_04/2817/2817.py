# 부분 수열의 합
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0    # 합이 k가 되는 모든 수
    for i in range(1 << N):   # 부분집합을 표시할 i
        s = 0   # 부분 집합의 합
        for j in range(N):  # j번 비트
            if i & (1 << j):   # j번 비트를 검사
                s += arr[j]
        if s == K:
            cnt += 1
    print(f'#{tc} {cnt}')
