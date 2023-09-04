# 구간 정리
# 스위치의 상태를 바꿀 함수
import sys
# import time
# start = time.time()
input = sys.stdin.readline

# 스위치 배열이랑 / 인덱스
def change_switch(position):
    if switch[position] == 0:
        switch[position] = 1
    else:
        switch[position] = 0

# n은 성별 m은 좌표값
def check_switch(n, m):
    # 오른쪽으로 왼쪽으로 검사하기
    dr = 1
    dl = -1
    arr_len = T

    # 남자일때
    if n == 1:
        k = 1
        while m * k < arr_len:
            change_switch(m * k - 1)
            k += 1
    # 여자일때
    else:
        nr = m - 1 + dr  # 4 5
        nl = m - 1 + dl

        while nr < arr_len and nl >= 0:
            if switch[nr] == switch[nl]:
                change_switch(nr)
                change_switch(nl)
                nr += 1
                nl -= 1
        change_switch(m-1)

# 스위치의 갯수
T = int(input())
# 스위치의 배치
switch = list(map(int, input().split()))
# 학생의 수
N = int(input())
# 학생들을 저장하고 검사
inpo = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    check_switch(inpo[i][0], inpo[i][1])

count = 0  # count 변수 초기화
for i in range(T):
    print(switch[i], end=' ')  # 스위치 상태 출력
    count += 1
    if count % 20 == 0:
        print()
#print("time :", time.time() - start)