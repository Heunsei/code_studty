N = int(input())


count = 0
for i in range(1, N+1):

    if i < 100:
        count += 1
    else:
        arr = []
        tmp = i
        while tmp != 0:
            to_add = tmp % 10
            arr.append(to_add)
            tmp //= 10

        checker = arr[1] - arr[0]
        isCont = True
        for n in range(1, len(arr)):
            if checker != arr[n] - arr[n-1]:
                isCont = False
        if isCont:
            count += 1
print(count)


