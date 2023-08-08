# 보이어 무어 (별세개)
# 뒤에서 부터 찾아보자
# 다음 조사위치를 패턴의 인덱스로 맞춰서 변경

# char : target의 값이 내 pattern에 몇번째에 있는지 조사
import sys
sys.stdin = open('input.txt')

def serch(pattern, char):
    # 동일한 값을 가지고 있는지 확인
    for i in range(len(pattern)-2, -1, -1):
        if pattern[i] = char:
            # 위치까지 이동하도록 index번호 넘겨주기
            return len(pattern) -i - 1 # 인덱스라 1 빼서
    # char pattern 일치 x
    return len(pattern)
    
def boyer_moore(pattern, target):
    result = 0
    # 조사 범위
    t_idx = 0
    while t_idx <= len(target) - len(pattern):
        # 뒤에서 부터
        p_idx = len(pattern)
        # p_idx 0이 되기 전까지
        while p_idx >= 0:
            # 비교하는게 서로다르다면
            if pattern[p_idx] != target[t_idx + p_idx]:
                # 다음조사로 옮길 값
                next = serch(pattern, target[t_idx+len(pattern) -1])
                break
            p_idx -= 1
        if p_idx == -1:
            count +=1
            t_idx += 1
        else:
            t_idx += next
    return result



for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
