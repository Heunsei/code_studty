# 다이얼
dials = ['ABC','DEF', 'GHI', 'JKL','MNO', 'PQRS', 'TUV', 'WXYZ']

numbers = list(input())
count = 0
for num in range(len(numbers)):
    for dial in dials:
        if numbers[num] in dial:
            count += dials.index(dial)+3
print(count)
    