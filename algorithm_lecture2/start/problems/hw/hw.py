import sys
sys.stdin = open('input.txt')

table = {
    '0001101': '0', '0011001': '1', '0010011': '2',
    '0111101': '3', '0100011': '4', '0110001': '5',
    '0101111': '6', '0111011': '7', '0110111': '8',
    '0001011': '9'
}

def get_pos(check):
    for i in range(N):
        for j in range(M-7):
            tmp = ''.join(check[i][j:j+7])
            tmp2 = ''.join(check[i][j+7:j+14])
            if str(tmp) in table and str(tmp2) in table:
                return [i, j]


T = int(input())
for tc in range(1, T+1):
    # N x M 의 직사각형
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = ''
    
    # code_pos[0] > 시작 i 좌표
    # code_pos[1] > 시작 j 좌표
    code_pos = get_pos(arr)
    #print('start_pos', code_pos)

    # 우리가 찾아야할 코드는 56자리
    code = ''.join(arr[code_pos[0]][code_pos[1]:code_pos[1]+56])
    #print(code)
    i = 0
    while i < 57:
        if i >= 55:
            break
        result += table[code[i:i+7]]
        i += 7
    res_list = list(result)
    ans = 0
    even_num = 0
    odd_num = 0
    #print(res_list)

    for i in range(1, 9):
        ans += int(res_list[i-1])
        if i % 2 != 0:
            odd_num += int(res_list[i-1])
        else:
            even_num += int(res_list[i-1])
    #print(even_num)
    #print(odd_num)

    tmp = odd_num * 3 + even_num

    #print(tmp)
    #print(ans)
    if tmp % 10 == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} 0')