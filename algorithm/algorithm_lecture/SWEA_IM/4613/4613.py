T = int(input())


def chek_color(line, color):
    return line.count(color)

def first_blue(arr,color):
    min_blue = 0
    min_idx = 0
    for i in range(len(arr)):
        if arr[i].count(color) > min_blue:
            min_blue = arr[i].count(color)
            min_idx = i
    return min_idx

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    count = 0
    blue_idx = first_blue(arr, 'B')

    for i in arr[0]:
        if i != 'W':
            count += 1

    for i in arr[N-1]:
        if i != 'R':
            count += 1

    print(count)