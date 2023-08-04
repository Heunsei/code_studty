# test case > T
T = int(input())
for tc in range(1, T+1):
    word = list(input())
    rev = []
    for w in word[::-1]:
        rev.append(w)
    if word == rev:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
