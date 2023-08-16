# 스택으로 풀기

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * N
    visited = [0] * N  # 행의 방문 여부를 저장하는 리스트

    now = 0
    acc = 0

    stack = [(now, acc, visited[:])] # 매 조사 대상마다 visited 는 별개처리
    while stack:
        # 다음 조사 대상
        now, acc, visited = stack.pop()
        if acc > result:
            continue
        if now == N:
            if acc < result:
                result = acc
        else:
            for row in range(N):
                if visited[row] == 0:
                    new_visited = visited[:]
                    new_visited[row] = 1
                    stack.append((now + 1, acc + arr[now][row], new_visited))