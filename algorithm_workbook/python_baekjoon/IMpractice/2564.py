# 직사각형을 돌면서 길이의 최소값을 찾기
# 가로 세로길이
M, N = map(int, input().split())
# 상점의 수
T = int(input())
arr = []
result = 0
# 상점의 위치
for _ in range(T):
    # 1 : 북쪽, 2 : 남쪽, 3 : 서쪽, 4 : 동
    dir, pos = map(int, input().split())

    if dir == 3 or dir == 4:
        arr.append([dir, N - pos])
    else:
        arr.append([dir, pos])

dong_i, dong_j = map(int, input().split())

if dong_i == 3 or dong_i == 4:
    dong_j = N - dong_j

# 동근이의 위치에 따라 상점까지의 거리가 달라짐
# 동근이가 북 남 / 동 서로 케이스를 나눠서 min을 사용해서 구해보자

# 동근이의 위치, 상점의 위치를 저장한 배열
def check_position(dong_i, dong_j, arr):
    global result
    # 1,2일때, 3,4일때 나눠서
    if dong_i == 3 or dong_i == 4:
        for position in arr:
            # 포지션이 동쪽 서쪽에 있을때
            # 포지션에 동쪽 서쪽에 있고 동근이의 위치와 같고 다름을 판별
            # 다른위치에 있으면 세로길이와 위 아래로 갔을때 길이 더한거중 적은걸 result 에
            if position[0] == 3 or position[0] == 4:
                if position[0] == dong_i:
                    result += abs(dong_j - position[1])
                else:
                    route1 = M + dong_j + position[1]
                    route2 = M + (N - dong_j) + (N - position[1])
                    result += min(route1, route2)
            
            if position[0] == 1 or position[0] == 2:
                # 동근이가 서쪽에 있을 때
                if dong_i == 3:
                    # 상점이 북쪽
                    if position[0] == 1:
                        result += (N - dong_j) + position[1]
                    # 상점이 남쪽
                    else:
                        result += (dong_j + position[1])
                        
                # 동근이가 동쪽에 있을 때
                else:
                    # 상점이 북쪽
                    if position[0] == 1:
                        result += (N - dong_j) + (M - position[1])
                    # 상점이 남쪽
                    else:
                        result += (dong_j + M - position[1])
    # 동근이가 북 / 남에 있을때
    else:
        for position in arr:
            # 상점이 같은 북, 남에 있을때
            if position[0] == 1 or position[0] == 2:
                if dong_i == position[0]:
                    result += abs(dong_j - position[1])
                else:
                    route1 = N + dong_j + position[1]
                    route2 = N + (M-dong_j) + (M-position[1])
                    result += min(route1, route2)
            # 상점이 서 / 동에 있을때
            else:
                # 동근이가 북쪽
                if dong_i == 1:
                    # 상점이 서쪽
                    if position[0] == 3:
                        result += (N - position[1] + dong_j)
                    # 상점이 동쪽
                    else:
                        result += (M - dong_j + N - position[1])
                # 동근이가 남쪽
                else:
                    # 상점이 서쪽
                    if position[0] == 3:
                        result += (dong_j + position[1])
                    # 상점이 동쪽
                    else:
                        result += (M - dong_j + position[1])

check_position(dong_i, dong_j, arr)
print(result)