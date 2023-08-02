T = int(input())
for tc in range(1, T+1):
    case = int(input())
    array = [list(map(int, input().split())) for _ in range(case)]
    print(array)

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
