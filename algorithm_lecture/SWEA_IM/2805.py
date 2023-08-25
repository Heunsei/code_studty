T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    mid = N // 2
    ans = 0
    #print(arr)

    for i in range(N//2):
        if i == 0:
            ans += int(arr[i][mid])
        else:
            ans += int(arr[i][mid])
            for j in range(mid+1, mid + i + 1):
                #print('j', arr[i][j])
                ans += int(arr[i][j])
            for k in range(mid-1, mid - i - 1, -1):
                #print('k', arr[i][k])
                ans += int(arr[i][k])

    for i in arr[mid]:
        ans += int(i)

    for i in range(mid + 1, N):
        if i == N-1:
            ans += int(arr[i][mid])
        else:
            ans += int(arr[i][mid])
            for j in range(mid+1, mid + (N - i)):
                #print('j', arr[i][j])
                ans += int(arr[i][j])
            for k in range(mid-1, mid - (N - i), -1):
                #print('k', arr[i][k])
                ans += int(arr[i][k])
    print(f'#{tc} {ans}')
