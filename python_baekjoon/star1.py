#별찍기
T = int(input())
for i in range(T):
    print(' '*(T-i-1), end='')
    print('*' * ((2 * i) + 1))
for i in range(T-2, -1, -1):
    print(' ' * (T-i-1), end='')
    print('*' * ((i*2)+1))
