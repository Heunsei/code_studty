import sys
sys.stdin = open('input.txt')
for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    result = 0
    p_idx = 0
    for t_idx in range(len(target)-len(pattern)+1):
        if p_idx and t_idx + p_idx <= last_t_idx + len(pattern):
            continue

        for p_idx in range(len(pattern)):
            # 패턴이랑 타겟이 다르면 종료
            if pattern[p_idx] != target[t_idx + p_idx]:
                last_t_idx = t_idx
                p_idx = 0
                break
        else:
            result += 1
            # 찾은시점의 t 인덱스
            last_t_idx = t_idx
    print(result)