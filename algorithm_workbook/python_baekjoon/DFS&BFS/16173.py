import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def is_valid(i,j):
    return 0 <= i < N and 0 <= j < N

def DFS(pos_i, pos_j):
    stack = []
    start = arr[pos_i][pos_j]
    stack.append([pos_i+start, pos_j])
    stack.append([pos_i, pos_j+start])
    while stack:
        nxt_i, nxt_j = stack.pop()
        if is_valid(nxt_i, nxt_j) and arr[nxt_i][nxt_j] == 0:
            print("Hing")
            return
        if not is_valid(nxt_i, nxt_j):
            continue
        if is_valid(nxt_i, nxt_j) and arr[nxt_i][nxt_j] == -1:
            print("HaruHaru")
            return
        if is_valid(nxt_i, nxt_j):
                stack.append([nxt_i + arr[nxt_i][nxt_j], nxt_j])
                stack.append([nxt_i, nxt_j + arr[nxt_i][nxt_j]])
    print("Hing")
    return
DFS(0,0)



