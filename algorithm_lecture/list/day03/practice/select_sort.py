# 셀렉트 정렬
a = [15, 26, 45, 11, 54, 65]
N = len(a)

# arr의 길이
def select_sort(arr, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if arr[minIdx] > arr[j]:
                minIdx = j
            arr[i], arr[minIdx] = arr[minIdx], arr[i]

def bubble_sort(arr):
    N = len(arr)
    for i in range(N-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def count_sort(arr, k):
    result = [-1] * len(arr)
    count_arr = [0] * (k + 1)
    for i in range(len(arr)):
        count_arr[arr[i]] += 1
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    for i in arr:
        count_arr[i] -= 1
        result[count_arr[i]] = i
    return result

#bubble_sort(a)
print(count_sort(a, 65))