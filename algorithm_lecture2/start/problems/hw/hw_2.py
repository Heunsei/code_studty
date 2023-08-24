import sys
sys.stdin = open('input.txt')

asc = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
    '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
    '0110111': 8, '0001011': 9
}

def search():
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '0': continue
            tmp = []
            for k in range(j - 56 + 1, j, 7):
                tmp.append(asc[arr[i][k:k+7]])
            odd_num = tmp[0] + tmp[2] + tmp[4] + tmp[6]
            even_num = tmp[1] + tmp[3] + tmp[5] + tmp[7]

            if (odd_num * 3 + even_num) % 10 == 0:
                return odd_num+even_num
            else:
                return 0
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
