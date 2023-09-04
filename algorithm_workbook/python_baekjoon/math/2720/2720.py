# import sys
# sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(input())
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    if N // 25 != 0:
        quarter += N//25
        N -= (25 * quarter)

    if N // 10 != 0:
        dime += N // 10
        N -= (10 * dime)

    if N // 5 != 0:
        nickel += N // 5
        N -= (5 * nickel)

    if N // 1 != 0:
        penny += N // 1
        N -= (1 * penny)

    print(int(quarter), int(dime), int(nickel), int(penny))

