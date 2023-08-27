from collections import deque
import sys
input = sys.stdin.readline


# 벨트의 길이, 종료조건 k
N, K = map(int, input().split())
# 벨트의 내구도
A = deque(list(map(int, input().split())))
robot = deque([0] * N)

count = 0
ans = 0
# print(A)
# print(robot)

while 1:
    ans += 1
    A.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    if sum(robot) != 0:
        for i in range(N - 2, -1, -1):
            # 로봇이 있는 칸에서 다음 번베이어 벨트의 k값이 1 이상이고
            # 로봇의 다음칸이 1이 아니라면
            if robot[i] == 1 and A[i+1] >= 1 and robot[i+1] == 0:
                robot[i+1] = 1
                robot[i] = 0
                A[i + 1] -= 1
                if A[i + 1] == 0:
                    count += 1
        robot[-1] = 0
        if count >= K:
            break

    if robot[0] == 0 and A[0] >= 1:
        A[0] -= 1
        robot[0] = 1
        if A[0] == 0:
            count += 1
        if count >= K:
            break
print(ans)



