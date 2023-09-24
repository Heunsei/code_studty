import sys
sys.stdin = open('input.txt')


# y의 값과 total을 받아옴
def search(cnt, y, total):
    global result
    if cnt == N:
        # N번 돌았으면 돌아와야함
        # 마지막 소모량 더해주기
        total += arr[y][0]
        # 총합이 기존보다 작으면 갱신후 종료
        if total < result:
            result = total
            return
    # 한번이라도 커지면 종료
    if total > result:
        return
    # 돌아오는걸 남기고 진행
    for i in range(1, N):
        # (n,n) 이면 건너뛰기
        if not arr[y][i]:
            continue
        # 방문한 적이 없다면
        if not visited[i]:
            visited[i] = 1
            search(cnt + 1, i, total + arr[y][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 987654321
    search(1, 0, 0)
    print(f'#{tc} {result}')