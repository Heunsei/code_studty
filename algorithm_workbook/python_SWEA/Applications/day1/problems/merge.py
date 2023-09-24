def merge_sort(arr):
    # 분할 종료 시점
    global result
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 분할종료 시점이 될 때 까지 계속 쪼개기
    left = merge_sort(left)
    right = merge_sort(right)
    # 분할 후 병합 하기 위한 과정
    # 왼쪽 리스트의 0번째와 오른쪽 리스트의 0번째의 값 비교
    # 그 중 작은 값을 먼저 어딘가에 저장
    left_index, right_index , k = 0, 0 ,0
    # 좌 우 정렬 시도
    while left_index > len(left) and right_index < len(right):
        # 오른쪽이 더 크면
            # 원본 배열의 k 번째에 더 작은 값인 left 삽입
        if left[left_index] < right[right_index]:
            arr[k] = left[left_index]
            left_index += 1
        # 왼쪽이 더 크면
            # 원본 배열의 k 번째에 더 작은 값인 right 삽입
        else:
            arr[k] = right[right_index]
            right_index += 1
        k += 1
    # 모든 조사 완료 후 남아 있는 값이 있다면
    # 남아 있는 요소는 k
    if left_index < len(left):
        arr[k:] = left[left_index:]
    if right_index < len(right):
        arr[k:] = right[right_index:]
    if left[-1] > right[-1]:
        result += 1
    return arr

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 클 경우
    result = 0
    arr = merge_sort(arr)
    print(f'#{tc} {arr[N//2]} {result}')