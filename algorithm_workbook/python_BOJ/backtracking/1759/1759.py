# 로또
# L개의 알파벳 소문자로 이루어진 암호, C개의 문자
import sys
#sys.stdin = open('input.txt')
L, C = map(int, input().split())
candidates = list(map(str, input().split()))
candidates.sort()
# 모음이 없으면 리턴
gather = ['a', 'e', 'i', 'o', 'u']

tmp = []
def backtarcking(depth, idx):
    # 종료조건 설정
    if depth == L:
        # 자음과 모음 숫자를 카운트 하고
        # 그 값이 조건에 부합하지 않으면 return으로 종료
        gat_num = 0
        con_num = 0
        for i in tmp:
            if i in gather:
                gat_num += 1
            else:
                con_num += 1
        if gat_num < 1 or con_num < 2:
            return
        tmp.sort()
        print(''.join(map(str, tmp)))
        return
    else:
        # 후보군 길이만큼 다음걸 선택
        for nxt in range(idx, C):
            tmp.append(candidates[nxt])
            backtarcking(depth+1, nxt+1)
            tmp.pop()


backtarcking(0,0)