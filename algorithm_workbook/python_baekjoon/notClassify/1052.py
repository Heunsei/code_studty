import sys
# 물병
# N개의 물병 모든 물병에 물이 1리터씩
# N개의 물병을 합쳐서 K개를 넘지않는 비어있는 물병을 만듬
# 사야하는 물병의 최소값 출력
N, K = map(int, input().split())
# 2^n 만큼의 물병이 존재
answer = 0

while bin(N).count('1') > K:
    N += 1
    answer += 1

print(answer)