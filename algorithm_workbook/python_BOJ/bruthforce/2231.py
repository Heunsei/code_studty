T = int(input())
for i in range(1, T+1):
    tmp = i
    original_i = i
    while i != 0:
        tmp += i % 10
        i //= 10
    if tmp == T:
        print(original_i)
        break
    if original_i == T:
        print(0)