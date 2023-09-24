import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(str, input().split())
    arr = list(map(str, input().split()))
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    print(f'#{tc}')
    for key, num in dic.items():
        if key == 'ZRO':
            for i in range(num):
                print(key, end=' ')
    for key, num in dic.items():
        if key == 'ONE':
            for i in range(num):
                print(key, end=' ')
    for key, num in dic.items():
        if key == 'TWO':
            for i in range(num):
                print(key, end=' ')
    for key, num in dic.items():
        if key == 'THR':
            for i in range(num):
                print(key, end=' ')
    for key, num in dic.items():
        if key == 'FOR':
            for i in range(num):
                print(key, end=' ')
    for key, num in dic.items():
        if key == 'FIV':
            for i in range(num):
                print(key, end=' ')
    for key, num in dic.items():
        if key == 'SIX':
            for i in range(num):
                print(key, end=' ')
    for key, num in dic.items():
        if key == 'SVN':
            for i in range(num):
                print(key, end=' ')
    for key, num in dic.items():
        if key == 'EGT':
            for i in range(num):
                print(key, end=' ')
    for key, num in dic.items():
        if key == 'NIN':
            for i in range(num):
                print(key, end=' ')
    print()