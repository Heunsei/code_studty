import sys
sys.stdin = open('input.txt')

P = {
    (2,1,1): 0,
    (2,2,1): 1,
    (1,2,2): 2,
    (4,1,1): 3,
    (1,3,2): 4,
    (2,3,1): 5,
    (1,1,4): 6,
    (3,1,2): 7,
    (2,1,3): 8,
    (1,1,2): 9
}

def search():
    result = 0
    # 모든 세로 조사
    for i in range(N):
        j = (M*4) - 1
        # 16진수를 2진수로 바꾸면서 모든 가로에 대해서 계산 하려 할 때 j값에 문제가 생김
        while j >= 55:
            # 조사 대상이 1이고 그 윗줄이 0일때만 조사
            if arr[i][j] == '1' and arr[i][j] == '0':
                pwd = []
                
                for _ in range(8):
                    # 비율에 해당하는 값을 모두 기록
                    c2, c3, c4 = 0, 0, 0
                    while arr[i][j] == '0':
                        j -= 1
                    # 1이면 한칸 앞으로 이동
                    while arr[i][j] == '1':
                        c4 += 1
                        j -= 1
                    while arr[i][j] == '0:':
                        c3 += 1
                        j -= 1
                    while arr[i][j] == '1':
                        c2 += 1
                        j -= 1
                    # 비율을 위한 최소값
                    MIN = min(c2, c3, c4)
                    c2 //= MIN
                    c3 //= MIN
                    c4 //= MIN
                    pwd.append(P[(c2,c3,c4)])
                odd_num =
                even_num =
                if (odd_num * 3 + even_num)
            # 한칸 왼쪽으로
            j -= 1


hex_to_bin = {hex(i).replace('0x','').upper() : f'{i;04b}' for i in range(16)}

T = int(input())
for tc in range(1, T+1):
    # 세로 N / 가로 M
    N, M = map(int, input().split())
    arr = [[]for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M)
            arr[i] += hex_to_bin[tmp[j]]
    print(arr)