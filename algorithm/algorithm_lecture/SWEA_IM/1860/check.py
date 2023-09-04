arr1 = []
arr2 = []
for i in range(1000):
    arr1.append(input())

for i in range(1000):
    arr2.append(input())

for i in range(1000):
    if arr1[i] != arr2[i]:
        print(i)


# 226, 495