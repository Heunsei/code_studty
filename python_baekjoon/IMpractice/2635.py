# 양의 정수가 주어짐
# 양의 정수 중 하나를 선택

T = int(input())

max_count = 0
result = []
for i in range(1, T+1):
    temp = [T, i]
    ck = 0
    start = 100
    N = 1000
    while N >= 0:
        N = temp[ck] - temp[ck+1]
        if N >= 0:
            temp.append(N)
        ck += 1
    #print(result)

    if max_count < len(temp):
        max_count = len(temp)
        result = temp


print(len(result))
print(*result)

