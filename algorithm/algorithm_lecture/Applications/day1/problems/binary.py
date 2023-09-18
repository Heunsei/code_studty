T = int(input())


# 조사 방향이 필요
def binary_search(L, R, K, D):
    global result
    # 결국 중간값이 필요함
    mid = (L + R) // 2
    # 중간값의 위치가 대상이라면 좌우 반복하면서 찾아낸 대상 횟수 1 증가
    if A[mid] == K:
        result += 1
        return
    # target 이 중간보다 크면
        # 오른쪽으로 조사를 보낼 것
        # 이전에서 오른쪽으로 왔으면 종료
    if A[mid] < T:
        if D == 'right':
            return
        binary_search(mid+1, R, K, 'right')
    # 작으면?
        # 왼쪽으로 조사를 보낼 것
        # 이전에서 왼쪽으로 왔으면 종료
    else:
        if D == 'left':
            return
        binary_search(L, mid-1, K, 'left')

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int, input().split()))

    for idx in range(M):
        binary_search(0, N-1, B[idx], 'start')

    result = 0
    print(f'#{tc} {result}')