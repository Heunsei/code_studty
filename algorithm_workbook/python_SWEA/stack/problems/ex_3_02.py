V, E = map(int, input().split())
arr = list(map(int, input().split()))
adj_m = [[0] * (V+1) for _ in range(V+1)]

def dfs(n, V, adj_m):
    stack = []                  # stack 생성
    visited = [0] * V(1+1)      # visited 생성
    visited[n] = 1              # 시작점 방문 표시
    print(n)
    while True:
        for w in range(1, V):  # 정점에 인접하고 방문하지 않았을때
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n) 
                n = w  # 방문위치 조정
                print(n)
                visited[n] = 1
                break
        else:  # 다 돌았는데 break 안만났으면
            if stack:
                n = stack.pop()  # 갈림길을 빼옴
            else:  # 스택에서 뻬올 좌표가없음
                break


for i in range():
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = adj_m[v2][v1] = 1

dfs(1, V, adj_m)
