# N^2개의 방이 n n형태로 상하좌우 방중에서 다음방의 숫자가 1커야함
import sys
from collections import deque
sys.stdin = open('input.txt')
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def is_valid(i,j):
    return 0 <= i < N and 0 <= j < N
def search(i, j):
    global ans_val
    global ans_idx
    dq = deque([(i, j, 0)])
    while dq:
        a, b, d = dq.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            # 몇번 돌았는지
            nd = d + 1
            if is_valid(ni, nj) and not visited[ni][nj] and arr[ni][nj] - 1 == arr[a][b]:
                dq.append((ni, nj, nd))
                visited[ni][nj] = True
    # 더이상 옆에 방문할 애가 없으니 횟수 리턴하고 종료
    # print(arr[i][j], nd)
    if nd > ans_val:
        ans_val = nd
        ans_idx = arr[i][j]
    if nd == ans_val:
        if ans_idx > arr[i][j]:
            ans_idx = arr[i][j]

T = int(input())
for tc in range(1, T+1):
    ans_val = 0
    ans_idx = 987654321
    N = int(input())
    visited = [[False]*N for _ in range(N)]
    idx_con = []
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 순서따라 인덱스가 꼬임
            visited[i][j] = True
            search(i, j)

    print(f'#{tc} {ans_idx} {ans_val}')