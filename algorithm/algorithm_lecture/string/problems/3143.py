T = int(input())

def ans(str1, str2):
    # str1에 2가 얼마나 들어있는지를 확인
    t_idx = 0
    p_idx = 0
    result = 0
    target_len = len(str1)

    while t_idx < target_len:
        if str1[t_idx] != str2[p_idx]:
            t_idx -= p_idx
            p_idx = -1
            # p의 인덱스만큼 올렸으니 돌려받아야겠지?
        p_idx += 1
        t_idx += 1
        if p_idx == len(str2):
            result += 1
            p_idx = 0
    return result

for tc in range(1, 1+T):
    A, B = input().split()
    res = ans(A, B)
    submit = len(A) - len(B)*res + res
    print(f'#{tc} {submit}')