# 구간 정리
# 스위치의 상태를 바꿀 함수
import sys
input = sys.stdin.readline
# 스위치 배열이랑 / 인덱스
def change_switch(arr, position):
    if arr[position] == 0:
        arr[position] = 1
    else:
        arr[position] = 0

# n은 성별 m은 좌표값
def check_switch(arr, n, m):
    # 오른쪽으로 왼쪽으로 검사하기
    dr = 1
    dl = -1
    arr_len = len(arr)

    # 남자일때
    if n == 1:
        k = 1
        while m * k < arr_len:
            change_switch(arr, m * k - 1)
            k += 1
    # 여자일때
    else:
        k = 1
        nr = m - 1 + dr * k  # 4 5
        nl = m - 1 + dl * k

        while nr < arr_len and nl >= 0:
            if arr[nr] == arr[nl]:
                change_switch(arr, nr)
                change_switch(arr, nl)
                nr += 1
                nl -= 1
        change_switch(arr, m-1)
# 스위치의 갯수
T = int(input())
# 스위치의 배치
switch = list(map(int, input().split()))
# 학생의 수
N = int(input())
# 학생들을 저장하고 검사
inpo = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    check_switch(switch, inpo[i][0], inpo[i][1])

count = 0
for i in switch:
    if count == 20:
        print()
        count -= 20
        continue
    print(i,end=' ')
    count +=1
print("time :", time.time() - start)