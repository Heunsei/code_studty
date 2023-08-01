# 구간합
# n개의 정수가 들어있는 배열에서 이웃한 m개의 합 구하기
T = int(input())
for tc in range(1, T+1):
    i, j = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    #print(numbers)

    tmp_list = []
    max_tmp = 0
    min_tmp = 0

    # j는 구간의 갯수
    for m in range(len(numbers)-j+1):
        tmp = 0
        for num in range(m, m+j):
            tmp += numbers[num]
        tmp_list.append(tmp)

    #print(tmp_list)
    max_tmp = tmp_list[0]
    min_tmp = tmp_list[0]

    for num in tmp_list:
        if max_tmp < num:
            max_tmp = num
        if min_tmp > num:
            min_tmp = num
    #print(max_tmp)
    #print(min_tmp)
    print(f'#{tc} {max_tmp - min_tmp}')