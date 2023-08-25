import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    min_count = 987654321
    b_count = 0
    r_count = 0
    # 4이 4일때
    # 흰색의 길이 1,2
    for i in range(1, N-1):
        w_idx = 0
        w_count = 0
        while w_idx < i:
            w_count += (M - arr[w_idx].count('W'))
            w_idx += 1
            #print('w_count : ', w_count)
        # 흰색의 길이가 1 일때 파란색의 최대 길이 2
        # 흰색의 길이가 2 일때 파란색의 길이 1
        #print('w_count',w_count)
        for j in range(1, N-i):
            b_idx = i
            b_len = 0
            b_count = 0
            while b_len < j:
                b_count += (M - arr[b_idx].count('B'))
                b_idx += 1
                b_len += 1
            #print('b_count : ', b_count)

            #print('b_count', b_count)
            # 빨간색의 길이
            K = N - i - j
            r_len = 0
            r_count = 0
            r_idx = i + j
            while r_len < K:
                r_count += (M - arr[r_idx].count('R'))
                r_idx += 1
                r_len += 1
            #print('r_count : ', r_count)
            res = w_count + b_count + r_count
            min_count = min(min_count, res)
    print(f'#{tc} {min_count}')
