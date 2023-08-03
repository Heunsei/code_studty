# 이진탐색
# arr원본 배열, N배열길이, key :타겟
def binary_serch(arr, N, key):
    start = 0
    end = N-1
    mid = N // 2
    while start <= end: #시작지점이 끝보다 작은동안만
        mid = (start + end) //2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
    return False

numbers = list(range(1,30,2))
print(numbers)
N = len(numbers)
target = 25
print(binary_serch(numbers,N,target))
