# 최소 생산 비용
# N곳의 공장당 한가지씩 생산
# arr 의 col 을 depth 로 조절
def backtracking(depth, acc):
    global result
    if acc > result:
        return
    if depth == N:
        if acc< result:
            result = acc
            return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                backtracking(depth+1, acc+arr[depth][i])
                visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 987654321
    backtracking(0,0)
    print(f'#{tc} {result}')