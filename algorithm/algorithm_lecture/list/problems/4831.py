# 정류장
# T - TestCase
# k 이동가능정류장, n종점의 위치, m충전기
# 충전기가 있는 정류장 다음줄에 표시
T = int(input())
for tc in range(1, T+1):
    K, N, C = list(map(int,input().split(' ')))
    bus_charge = list(map(int,input().split(' ')))
    
    line = [0] * N
    for i in bus_charge:
        line[i] = 1
    print(line)
    
    count = 0
    now_position = K
    charge = 0
    while now_position < N:
        if line[now_position] == 1:
            count += 1
            charge = now_position
            now_position += K
        else:
            now_position -= 1
        
        if charge == now_position:
            count = 0
            break
    print(f'#{tc} {count}')