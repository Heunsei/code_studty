import sys
sys.stdin = open('input.txt')
for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    # 조사대상 2개 pattern / target
    p_idx = 0
    t_idx = 0
    # 결과, 패턴이 문장에 몇번??
    result = 0
    len_target = len(target)
    while t_idx < len_target:
        # 검사한 인덱스만큼 target 인덱스를 줄여줘야함
        if target[t_idx] != pattern[p_idx]:
            t_idx -= p_idx
            p_idx = -1
        p_idx += 1
        t_idx += 1
        if p_idx == len(pattern):
            result += 1
            p_idx = 0
    print(f'#{tc} {result}')
