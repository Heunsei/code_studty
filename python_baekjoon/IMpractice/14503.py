# 로봇청소기
def iswall(i, j):
    if room[i][j] == 1:
        return True

def clean(i, j):
    global ans
    if room[i][j] == 0:
        room[i][j] = 3
        ans += 1

def turndir(direction):
    if direction == 0:
        return 3
    elif direction == 1:
        return 0
    elif direction == 2:
        return 1
    else:
        return 2

def getback(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    else:
        return 1

def turnoff():
    global stop
    stop = True

# 현재 위치 기준으로 상하좌우를 검사
def checkdir(tmp_r, tmp_c, dir):
    global direction
    global r, c
    chk = 0
    for i in range(4):
        ni = tmp_r + di[i]
        nj = tmp_c + dj[i]
        if room[ni][nj] != 0:
            chk += 1
    if chk == 4:
        back = getback(dir)
        ni = tmp_r + di[back]
        nj = tmp_c + dj[back]
        if not iswall(ni, nj):
            r = ni
            c = nj
            return
        else:
            turnoff()
            return
    else:
        direction = dir
        while True:
            direction = turndir(direction)
            ni = tmp_r + di[direction]
            nj = tmp_c + dj[direction]
            if room[ni][nj] == 0:
                r, c = ni, nj
                #clean(ni, nj)
                break

def robot(r, c, direction):
    #print(r, c)
    clean(r, c)
    checkdir(r, c, direction)

N, M = map(int, input().split())

# 0 > 북, 1 > 동, 2 > 남, 3 > 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ans = 0
# 0은 청소되지 않은 상태, 1은 벽, 3은 청소됨
r, c, direction = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
stop = False

while stop != True:
    robot(r, c, direction)
print(ans)


