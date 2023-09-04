# 설탕배달
# 3kg 봉지와 5kg 으로 조합가능한 개수중 가장 작은걸 출력
T = int(input())

three = T // 3
five = T // 5
# 아무리 해봤자 5천 못넘음
result = 5000

for i in range(1, three + 1):
    tmp = T - (3 * i)
    count = i
    if tmp % 5 != 0:
        count = -1
    elif tmp > 0 and tmp % 5 == 0:
        count += tmp // 5

    if count != -1 and result > count:
        result = count

for n in range(1, five + 1):
    tmp = T - (5 * n)
    count = n
    if tmp % 3 != 0:
        count = -1
    elif tmp > 0 and tmp % 3 == 0:
        count += tmp // 3
    if count != -1 and result > count:
        result = count

if result == 5000:
    print(-1)
else:
    print(result)