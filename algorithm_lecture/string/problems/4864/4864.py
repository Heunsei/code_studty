import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    key = input()
    compare = input()
    #print("key", key)
    #print("compare", compare)
    N = len(key)
    index = []

    for i in range(len(compare)):
        if compare[i] == key[0]:
            index.append(i)

    print(f'index:{index}')
    count = 0
    for i in index:
        for j in range(N):
            if compare[i+j] != key[j]:
                continue
        if j == N-1:
            count += 1
    print(count)