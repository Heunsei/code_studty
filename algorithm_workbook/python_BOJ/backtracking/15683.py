def backtracking(depth):
    pass


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 바라보는 방향으로 쭉 확인가능
# 1,3,4 는 3번까지 회전
# 2번은 두번까지 회전
