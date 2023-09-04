# 종이자르기
dic = {0: 0, 1: 1, 2: 3}

def add_papaer(n):
    if n in dic:
        return dic[n]
    else:
        dic[n] = add_papaer(n-1) + add_papaer(n-2) * 2
        return dic[n]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    result = add_papaer(n//10)
    print(f'#{tc} {result}')