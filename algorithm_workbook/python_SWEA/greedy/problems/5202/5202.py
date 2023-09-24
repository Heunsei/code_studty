T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time_list = []
    for _ in range(N):
        start, end = map(int, input().split())
        time_list.append((start, end))
    ans = 0
    time_list.sort(key=lambda x: x[1])
    #print(time_list)
    for i in range(N):
        tmp = 1
        end = time_list[i][1]
        for j in range(i+1, N):
            if time_list[j][0] >= end:
                tmp += 1
                end = time_list[j][1]
        if ans < tmp:
            ans = tmp
    print(f'#{tc} {ans}')