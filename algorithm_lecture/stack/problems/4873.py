# 연속된 문자 지우기
T = int(input())
for tc in range(1, T+1):
    tmp = []
    for i in input():
        if len(tmp) == 0:
            tmp.append(i)
            print(tmp, 'input :', i)
        else:
            if i == tmp[-1]:
                tmp.pop()
                print(tmp, 'input :', i)
            else:
                tmp.append(i)
                print(tmp, 'input : ', i)
    N = len(tmp)
    print(f'#{tc} {N}')