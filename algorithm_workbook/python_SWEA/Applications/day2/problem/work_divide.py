# SWEA HW 동철이의 일분배
# 순열을 구하는 문제

def perm(depth, acc):
    global result
    if acc<= result:
        return
    if depth == N:
        if acc > result:
            result = acc
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                perm(depth + 1, acc * arr[depth][i])
                visited[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visited = [False] * N
    # 비교대상
    result = 0
    # 각 위치의 정수 pi는 확률
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         arr[i][j] /= 100
    arr = [list(map(lambda x:int(x)/100, input().split()))for _ in range(N)]
    perm(0,1)
    result = result * 100
    print(f'#{tc} {result:7f}')
