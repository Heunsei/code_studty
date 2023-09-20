
def bfs(S, cnt):
    # S 탐색 시작 번호
    # 노드까지 도달하는데 걸린시간
    q = [S, 0]
    visited[S] = 1
    while q:
        S, cnt = q.pop(0)
        # 현재 조사 대상 S 노드가 진출 차수가 없다면 빈리스트 반환 -> 순회 x
        for i in G.get(S, []):
            if not visited[i]:
                visited[i] = cnt + 1
                q.append((i, cnt + 1))
    return S


# 마지막으로 연락받은 대상의 번호를 출력
    # 마지막으로 연락받은 사람이 여러명으면, 출석 번호가 높은 사람을 반환.
for tc in range(1,11):
    # 시작 정점 S로 부터 시작해서
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    # 학생은 1~100까지 존재
    visited = [0] * 101

    G = {}
    # 방향서 있는 그래프
    for i in range(N//2):
        # G.get(1,[])을 찾아봄 : G의 key가 1인값이 없으면 빈리스트 반환
        # G.get(1,[]) + [2] -> G = {1:[2]}
        G[arr[i*2]] = G.get(arr[i*2], []) + [arr[i*2+1]]
    last = bfs(S)
    # 출석 번호가 가장 높은걸 찾고 종료하면됨
    for i in range(100, -1, -1):
        if visited[i] == visited[last]:
            print(f'#{tc} {i}')
            break
