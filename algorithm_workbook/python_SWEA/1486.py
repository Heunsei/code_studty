def make_top(depth, acc):
    global res
    if depth == N:
        if acc >= B:
            res = min(res,acc-B)
        return
    make_top(depth+1, acc + arr[depth])
    make_top(depth+1, acc)


T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    arr = list(map(int,input().split()))
    candidate = []
    res = 987654321
    make_top(0,0)
    print(f'#{tc} {res}')
