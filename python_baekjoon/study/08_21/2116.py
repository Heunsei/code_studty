T = int(input())
arr = []
for _ in range(T):
    arr.append(list(map(int, input().split())))

# A,B,C,D,E,F 순으로 입력
# A-F (1,6), B-D (2,4) , C-E(3,5) 연결
# 맨 아래에 가장작은값이 오도록..?

print(arr)