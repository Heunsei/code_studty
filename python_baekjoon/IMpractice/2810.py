# 컵홀더
N = int(input())
seat = input()
seat_len = len(seat)
cnt = 1
i = 0
while True:
    if i == seat_len:
        if cnt > N:
            print(N)
        else:
            print(cnt)
        break

    if seat[i] == "S":
        cnt += 1
        i += 1
    elif seat[i] == "L":
        cnt += 1
        i += 2
