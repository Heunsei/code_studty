arr = [1, 5, 3, 2, 6, 1, 21, 53, 42]
M = max(arr)
def bubble_sort(array):
    N = len(array)
    for i in range(N-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def counting_sort(array, M):
    # 최대값의 +1만큼 배열생성
    check = [0] * (M+1)
    # 결과값을 저장할 배열
    result = [-1] * len(arr)

    for i in range(len(array)):
        check[arr[i]] += 1
    # 누적합 구하기
    for i in range(1, len(check)):
        check[i] += check[i-1]
    # array의 원소들을 순회하면서
    for num in array:
        check[num] -= 1
        result[check[num]] = num
    return result


print(counting_sort(arr,M))
print(bubble_sort(arr))