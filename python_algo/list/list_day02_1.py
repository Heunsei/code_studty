#11092

# N개의 양의 정수가 첫번째부터 N번째까지 주어짐

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr= list(map(int, input().split()))

    min_idx = 0 # 최소의 index
    max_idx = 0 # 최대의 index
    for i in range(1, N):
        if arr[min_idx] >= arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i
    ans = 0
    if max_idx > min_idx:
        ans = max_idx - min_idx
    else:
        ans = min_idx - max_idx
    print(f'#{T} {ans}')