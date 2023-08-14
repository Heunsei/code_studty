arr = list(range(1, 11))
n = len(arr)

print(n)
for i in range(1 << n):
    # 모든 경우의 수에 대해서
    # 만들 수 있는 부분집합
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    if sum(subset) == 10:
        print(subset)