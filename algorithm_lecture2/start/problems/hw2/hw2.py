import sys
sys.stdin = open('input.txt')
# 배열은 16진수로 이루어져 있음 이를 2진수로바꿔서 코드 정보 확인
# 비정상적인 암호가 섞여 있을 수도 있다

def get_start(arr):
    for i in range(len(arr)-1):
        if arr[i] == "1":
            return i
    return 0
to_bin = {
    '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111'
}


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 16진수를 2진수로 변환해서 넣어둔 배열
    tmp = [input() for _ in range(N)]
    arr = []


    for i in range(N):
        t = ''
        for j in range(M):
            if tmp[i][j] in to_bin:
                t += to_bin[tmp[i][j]]
            else:
                t += '0'
        arr.append(t)

    for i in arr:
        print(i)
    for c in arr:
        print(c)
        temp = c[::-1]
        #print(len(temp)
        start_pos = get_start(temp)
        #print('start', start_pos)
        code_list = []
        code_ratio = []
        change_count = 0
        num_count = 0
        isChange = False
        #print(temp)
        for idx in range(start_pos, len(temp)):
            if idx > start_pos and temp[idx] != temp[idx-1]:
                change_count += 1
                code_ratio.append(num_count)
                #print(code_ratio)
                if len(code_ratio) == 4:
                    code_list.append(code_ratio)
                if len(code_ratio) == 31:


                    print(code_ratio)
                num_count = 1
            else:
                num_count += 1

