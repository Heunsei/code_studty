def order(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    order(left[node])
    order(right[node])


T = int(input())
for tc in range(1, T+1):
    # 간선의 개수 E와 탐색 시작점 N
    E, N = map(int, input().split())
    # 노드의 개수
    V = E + 1
    # 간선정보
    arr = list(map(int, input().split()))

    left = [0] * (V+1)
    right = [0] * (V+1)
    cnt = 0
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    order(N)
    print(f'#{tc} {cnt}')