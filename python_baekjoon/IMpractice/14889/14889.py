# 백트래킹을 이용한 방법


import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [False for _ in range(n)]  # 1차원으로 방문 리스트 생성
min_value = sys.maxsize  # 최소값을 갱신 할 변수

def backTracking(depth, idx):  # 깊이를 나타내는 변수와 인덱스
    global min_value
    print(depth)
    print(visit)
    if depth == n // 2:  # n은 짝수로 주어지니까 수의 절반이 선택되었을때 시작
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:  # True를 스타트팀
                    power1 += graph[i][j]
                elif not visit[i] and not visit[j]:  # False를 링크팀
                    power2 += graph[i][j]
        min_value = min(min_value, abs(power1 - power2))

        return

    for i in range(idx, n):  # 조건이 안맞으면 백트래킹 시작
        if not visit[i]:
            visit[i] = True
            backTracking(depth+1, i+1)  # 같은 번호 호출 방지
            visit[i] = False
backTracking(0, 0)
print(min_value)