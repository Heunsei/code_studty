# ACM craft
from collections import deque
T = int(input())

# 위상정렬 개념이 필요한 문제
for tc in range(T):
    # 건물의 개수 N, 건설규칙의 종류 K
    N, K = map(int, input().split())
    # 건물별 연결된 빌드
    build = [[] for _ in range(N+1)]
    # 진입차수를 관리할 리스트
    indegree = [0] * (N + 1)
    # 건물별 걸리는 시간 0번쨰 리스트는 비어있을거고 1부터쓸거니까
    delay = [0] + list(map(int, input().split()))
    # 건물까지 걸리는 시간
    DP = [0 for _ in range(N+1)]

    for _ in range(K):
        a, b = map(int, input().split())
        build[a].append(b)
        indegree[b] += 1
    # 종료 조건
    V = int(input())

    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            DP[i] = delay[i]
    while q:
        a = q.popleft()
        for i in build[a]:
            indegree[i] -= 1
            # 1 ,2, 3, 4 기준
            # 10초 1초 100초 10초필요
            # 전에있던(연결이 여러개니까) 합이랑
            # 이번의 합을 비교해서 큰걸 DP[i]에 넣어줌
            # 2에는 11 3에는 110 저장
            # 4에 11 + 10 이랑 110 + 10 비교해서 큰걸 저장
            DP[i] = max(DP[a] + delay[i], DP[i])
            if indegree[i] == 0:
                q.append(i)
    print(DP[V])