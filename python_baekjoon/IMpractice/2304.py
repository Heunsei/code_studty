N = int(input())
arr = [0] * 1001
# 출력할 최종값
tot = 0
for _ in range(N):
    N, L = map(int, input().split())
    arr[N] = L

max_L = max(arr)
max_idx = arr.index(max_L)
max_positions = []

for i in range(len(arr)):
    if arr[i] == max_L:
        max_positions.append(i)

if len(max_positions) > 1:
    right_max_position = max_positions[-1]
else:
    right_max_position = max_idx

# 제일 큰 막대를 기준으로 좌 / 우 너비를 구하고
# 가장큰걸 넣어줌
#print(arr)
left_max = 0
current = 0
for i in range(0, max_idx+1):
    if left_max < arr[i]:
        tot += (i - current) * left_max
        current = i
        # print('current ', current)
        # print('idx ', i)
        # print('total', tot)
        left_max = arr[i]

#print(tot)
# 오른쪽에서의 긴 기둥의 길이
right_max = 0

current2 = 1001
for i in range(1000, right_max_position-1, -1):
    if right_max < arr[i]:
        tot += (current2 - i) * right_max
        current2 = i
        # print('----------------')
        # print('rMAX', right_max)
        # print('current2 ', current)
        # print('idx2 ', i)
        # print('total2', tot)
        # print('----------------')
        right_max = arr[i]
# print(max_positions)
# print(max_L)
if len(max_positions) > 1:
    tmp = (max_positions[-1] - max_positions[0] + 1) * max_L
    print(tot + tmp)
else:
    print(tot+max_L)