arr = [1, 5, 4, 3, 2, 6, 1, 11, 24, 2, 4, 5, 6]
max_arr = -1
result = [-1] * len(arr)

for i in arr:
    if i > max_arr:
        max_arr = i

check_arr = [0] * (max_arr + 1)

for i in range(len(arr)):
    check_arr[arr[i]] += 1

for i in range(1, len(check_arr)):
    check_arr[i] += check_arr[i-1]

# arr을 순회하면서 값넣기
for num in arr:
    check_arr[num] -= 1
    result[check_arr[num]] = num

print(result)
