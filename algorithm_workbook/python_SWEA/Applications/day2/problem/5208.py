# 전기버스 2
def search(r, acc, gas):
    global result
    if acc >= result:
        return
    if r == N-1:
        if acc < result:
            result = acc
        # 충전 횟수
    else:
        if gas:
            search(r+1, acc+1, gas - 1)
        search(r+1,acc, arr[r] - 1)


T = int(input())
for tc in range(1,T+1):
    N, *arr = list(map(int, input().split()))
    # 모든 정류소에서 충전을 한 것이 최악의 상황
    result = N
    search(1, 0, arr[0]-1)
    print(f'#{tc} {result}')