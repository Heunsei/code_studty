# 위치옮기기
import sys
input = sys.stdin.readline

# 델타탐색으로 접근하니 메모리초과 시간초과뜨고 난리남
# > 문제에서 제시간 테스트케이스의 개수가 너무 많아서 
# 식으로 계산해서 접근해야함
W, H = map(int, input().split())
x, y = map(int, input().split())
t = int(input())
result_x = 0
result_y = 0
# a와 b로 x,y 좌표가 몇번 돌수 있는지 확인
a = (x + t) // W
b = (y + t) // H
# a가 2로 나누어 떨어지면
if a % 2 == 0:
    result_x = (x + t) % W
else:
    result_x = W - (x + t) % W

if b % 2 == 0:
    result_y = (y + t) % H
else:
    result_y = H - (y + t) % H

print(f'{result_x} {result_y}')