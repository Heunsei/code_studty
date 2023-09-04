import sys
sys.stdin = open('input.txt')

def check_string(compare, pattern):
    t_idx = 0
    p_idx = 0
    t_len = len(compare)
    while t_idx < t_len:
        if compare[t_idx] != pattern[p_idx]:
            t_idx -= p_idx
            p_idx = -1
        t_idx += 1
        p_idx += 1
        if p_idx == len(pattern):
            return True
    return False

T = int(input())
for tc in range(1, T+1):
    pat = input()
    compare = input()
    if check_string(compare, pat):
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
