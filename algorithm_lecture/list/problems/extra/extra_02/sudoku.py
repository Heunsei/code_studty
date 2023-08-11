T = int(input())

def check():
    cnt = 0
    for i in range(9):
        tmp_i = []
        tmp_j = []
        for j in range(9):
            tmp_i.append(arr[i][j])
            tmp_j.append(arr[j][i])
        if len(set(tmp_i)) != 9 or len(set(tmp_j)) != 9:
            return False
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            tmp = []
            tmp.extend(arr[i][j:j+3])
            tmp.extend(arr[i+1][j:j+3])
            tmp.extend(arr[i+2][j:j+3])
            if len(set(tmp)) != 9:
                return False
    return True

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    if check():
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')



