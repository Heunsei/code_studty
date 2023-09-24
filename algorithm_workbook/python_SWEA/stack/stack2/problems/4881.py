# 행, 열마다 하나씩 숫자를 선택해서 합을 구하는 문제
# 재귀쓰는거도 결국은 while 문과 똑같다

def make_candidates(visited, now, C):
    # 이 행을 지나갔는지 표시
    in_perm = [False] * NMAX
    # 하나하나 순회할거
    for i in range(1, now):
        in_perm[visited[i]] = True
    # 후보 계수 초기화
    ncands = 0
    # 순열정보에 대해 그 위치가 False 라면
    for i in range(1, N+1):
        if in_perm[i] == False:
            c[ncands] += 1
            ncands += 1
    return ncands
        

def backtrack(visited, now, end, acc):
    global = result
    if acc > result:
        return
    # 조사 종료시점
    c = [0] * MAXCANDIDATES

    if now == end: # 모든 열에 대해서 조사가 가능
        if acc < result:
            result = acc
    # 조사할게 남았으면 다음 위치 조사
    else:
        now += 1
        # 현재 위치의 후보 생성
        ncands = make_candidates(visited, now, C) # 후보군 생성 후 후보군의 길이 반환
        # 후보군 범위 안에서
        # c의 i번째를 넣어줄거, 순열의 정보가 들어있다
        for i in range(ncands):
            visited[now] = c[i]
            backtrack(visited, now, end, acc + arr[now -1][visited[now]-1])
            # 다른 후보군 조사를 위해 초기화
            visited[now] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 최종 결과값, 각 행, 열의 값들의 합의 최소
    result = 10 * N
    MAXCANDIDATES = N # 최대 후보군 수
    NMAX = N + 1
    visited = [False] * NMAX
    # 방문표시, 시작점, 끝점, 누적값
    backtrack(visited, 0, N, 0)
    print(f'#{tc} {}')