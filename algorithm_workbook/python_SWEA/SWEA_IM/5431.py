# 테스트케이스의 수
T = int(input())
for tc in range(1, 1+T):
    # 전체 수강생 수 / 과제를 제출한 사람
    N, M = map(int, input().split())
    res = [i for i in range(1, N + 1)]
    arr = list(map(int, input().split()))

    for i in arr:
        res.remove(i)

    print(f'#{tc}', end=' ')
    print(*res)