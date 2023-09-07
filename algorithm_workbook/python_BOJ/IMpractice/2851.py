# 10개의 버섯을 먹어서 점수가 100에 가장 가깝게 나오도록

count = 0
to_print = 0
dif = 100
for _ in range(10):
    count += int(input())
    tmp = abs(count - 100)
    if tmp <= dif:
        dif = tmp
        to_print = count
print(to_print)