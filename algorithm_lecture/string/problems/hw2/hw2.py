import sys
sys.stdin = open('input.txt')

def check_pali(arr):
    arr_len = len(arr)
    for i in range(arr_len//2):
        if arr[i] != arr[arr_len - i - 1]:
            return False
    return True

for tc in range(1, 11):
    word_len = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0
    #print(arr)
    for i in range(8):
        for j in range(9-word_len):
            tmp = []
            for m in range(word_len):
                tmp.append(arr[i][j+m])
            if check_pali(tmp):
                count += 1

    for j in range(8):
        for i in range(9-word_len):
            tmp = []
            for m in range(word_len):
                tmp.append(arr[i+m][j])
            if check_pali(tmp):
                count += 1

    print(f'#{tc} {count}')
