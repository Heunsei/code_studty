T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = [0] * 8

    first = N // 50000
    result[0] += first
    N %= 50000

    second = N // 10000
    result[1] += second
    N %= 10000

    third = N // 5000
    result[2] += third
    N %= 5000

    forth = N // 1000
    result[3] += forth
    N %= 1000

    fifth = N // 500
    result[4] += fifth
    N %= 500

    sixth = N // 100
    result[5] += sixth
    N %= 100

    seventh = N // 50
    result[6] += seventh
    N %= 50
    eighth = N // 10
    result[7] += eighth
    N %= 10
    print(f'#{tc}')
    print(*result)
