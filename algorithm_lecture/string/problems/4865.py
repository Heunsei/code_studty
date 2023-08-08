T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = input()
    dic = {}

    compare = list(set(str1))
    # compare에 있는 값만 더하기
    for i in str2:
        if i in compare:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
    result = max(dic.values())
    print(f'#{tc} {result}')