import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 사람의 수 / 시간 / 붕어빵
    N, M, K = map(int, input().split())
    peoples = list(map(int, input().split()))
    peoples.sort()
    is_possible = True
    time = 0
    time_peoples = max(peoples)
    bread = 0
    idx = 0
    while time < time_peoples+1:
        if time and time % M == 0:
            bread += K
        if peoples[idx] == time:
            if bread > 0:
                bread -= 1
                idx += 1
            else:
                is_possible = False
                print(f'#{tc} Impossible')
                break
        time += 1
    if is_possible:
        print(f'#{tc} Possible')
