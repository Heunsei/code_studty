# 노드문제
import sys
input = sys.stdin.readline

T = int(input())

def DFS(start, end):
    # 정점의 갯수만큼 검사할것임
    for nxt in range(1, V+1):
        if adj[start][nxt] == 1 and not visited[nxt]:
            visited[nxt] = True
            if nxt == end:
                global is_there
                is_there = True
                break
            # 일단 행을(i)늘려가면서 아래로
            DFS(nxt, end)

for tc in range(1, T+1):
    # 노드, 간선정보개수
    V, E = map(int, input().split())
    # 체커
    visited = [False] * (V+1)
    # 연결표시하는 리스트 adj
    adj = [[0] * (V+1) for _ in range(V+1)]
    is_there = False

    # 간선 정보 갯수만큼 for 문 돌면서 adj 에 값 표기
    for i in range(E):
        a, b = map(int, input().split())
        adj[a][b] = 1


    # 마지막에 받는 시작값과 찾아야 하는 끝값
    start, end = map(int, input().split())

    DFS(start, end)
    if is_there:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')