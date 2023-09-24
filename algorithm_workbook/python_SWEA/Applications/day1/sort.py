# 가장 오른쪽 원소를 pivot 으로 잡음
# 분할해서 정복할 것중에서 가장 오른쪽에 있는걸 pivot 으로
# pivot
def quick_sort(arr,left, right):
    # 분할 정복의 가장 핵심
    if left < right:
        mid = cal(arr, left, right)
        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid+1, right)

# lomuto > pivot 을 가장 오른쪽 원소로 결정
def cal(arr, left, right):
    # pivot 보다 큰 구간의 왼쪽 경계
    i = left -1
    # pivot 보다 큰 구간의 오른쪽 경계
    j = left
    pivot = arr[right]
    while j < right:
        # pivot 이 j번째 값보다 크면
        if pivot > arr[j]:
            i += 1
            # i 와 i 사이에 pivot 보다 큰 값이 있다
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i+1], arr[right] = arr[right], arr[i + 1]
    print(arr)
    return i + 1



nums = [15, 53, 23, 51, 27, 34]
