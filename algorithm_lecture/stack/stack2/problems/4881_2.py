T = int(input())

def search(now, acc):
    global  result
    # 가지치기는 똑같이 진행
    # 누적값이 최종 결과보다 한번이라도 커지면, 더이상 조사 x
    if acc > result:
        return
    # now 가 N 이되면 탐색끝이라 판단해도 됨
    if now == N:
        if acc < result:
            result = acc
        else:
            # 현재 now 열에서 모든 행 row 를 탐색할것
            # for 는 N 번만큼 돌릴건데
            # now가 0일때 깊이 들어가서 2일때 row 123...N까지돌리고
            # now가 1일때로 돌아와서 123...N까지 돌리고
            # now가 0으로 돌아와서 row를 돌리는것
            for row in range(N):
                # 방문을 안했더라면
                if visited[row] == 0:
                    visited[row] = 1  # 현재값을 쓰고 다음조사 하러갈거다
                    # acc + arr[now][row] now 열 의 row 값을 더하고
                    # search 를 다시불러 now + 1해서 다음 열을 검사
                    search(now + 1, acc + arr[now][row])
                    visited[row] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * N
    visited = [0] * N  # 행의 방문 여부를 저장하는 리스트

    # 시작점, 누적값
    
    print(f'#{tc} {result}')