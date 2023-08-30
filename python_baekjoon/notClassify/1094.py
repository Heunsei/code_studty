from collections import deque

X = int(input())
stick = [64]
num_of_stick = 1
cnt = 1
while True:
    if sum(stick) == X:
        break
    if sum(stick) > X:
        to_cut = stick.pop(0)
        tmp = []
        to_cut /= 2
        tmp.append(to_cut)
        tmp.append(to_cut)
        if to_cut + sum(stick) >= X:
            stick.append(to_cut)
        else:
            stick.extend(tmp)
    stick.sort()
print(len(stick))

