from collections import deque
# 이중리스트의 1열만 돌면서 확인
def search(x):
    check = [0]*N
    dq = deque()
    dq.append((x))
    while dq:
        cur = dq.popleft()
        for next in range(N):
            if not check[next] and arr[cur][next] == 1:
                check[next] = 1
                dq.append(next)
    print(*check)


    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    search(i)



