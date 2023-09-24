# using LPS
# using KMP
# 패턴을 조사하면서 배열을 찾아버리는것
# 조사하다가 그안에 패턴이 없거나 중간에 끊겨버리면
# 다시 조사해야하니까 너무 기찬타
import sys
sys.stdin = open('input.txt')

def make_lps(pattern):
    lps = [0] * len(pattern)
    # 이전패턴 정보누적값을 담기위한 인덱스
    lps_idx = 0
    for i in range(1, len(pattern)):
        # 이전번 글자와 현재 글자가 같다면
        if pattern[lps_idx] == pattern[lps_idx]:
            # 이전에 나랑 같던게 하나있다
            lps[i] = lps_idx + 1
            lps_idx += 1
        else:  # 다를 때 다시비교
            lps_idx = 0
            if pattern[lps_idx] == pattern[lps_idx]:
                lps[i] = lps_idx + 1
                lps_idx += 1
    return lps

def KMP(pattern,taget):
    lps = make_lps(pattern)
    # 조사는 brute force랑 똑같이
    p_idx = 0
    t_idx = 0
    result = 0
    while t_idx < len(target):
        if pattern[p_idx] == target[t_idx]:
            p_idx += 1
            t_idx += 1
        else:
            if p_idx == 0:
                t_idx += 1
            else:
                p_idx = lps[p_idx-1]
        if p_idx == len(pattern):
            result += 1
            p_idx = 0
    return result
for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
