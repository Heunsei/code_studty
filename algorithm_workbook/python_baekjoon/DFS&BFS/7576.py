from collections import deque


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
tmt = deque([])

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
count = 1


def id_valid(i, j):
    return 0 <= i < N and 0 <= j < M

num_of_zero = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tmt.append((i, j))
        elif box[i][j] == 0:
            num_of_zero += 1

if num_of_zero == 0:
    print('0')

while tmt:
    for i in range(len(tmt)):
        a, b = tmt.popleft()
        for k in range(4):
            ni = a + di[k]
            nj = b + dj[k]
            if id_valid(ni, nj) and box[ni][nj] == 0:
                tmt.append((ni, nj))
                box[ni][nj] = 1
                num_of_zero -= 1
                if num_of_zero == 0:
                    print(count)
                    break
    count += 1

if num_of_zero != 0:
    print('-1')


# print(count)
