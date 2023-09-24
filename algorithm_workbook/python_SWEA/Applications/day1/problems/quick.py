def quick_sort(arr):
    pass
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = quick_sort(arr)
    print(f'#{tc} {result[N//2]}')