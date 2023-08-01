# 매개변수 필요
# 입력배열 : numbers
# 최대값 : k

def counting_sort(numbers, k):
    # result의 범위 : 전체 numbers 원소 만큼
    result = [-1] * len(numbers)
    count_arr = [0] * (k+1)

    for i in range(len(numbers)):
        # numbers[i]를(숫자임) 인덱스로 하는 count의 값 +1
        count_arr[numbers[i]] += 1

    # 각 요소가 들어가야할 인덱스를 계산
    # 누적값 카운트
    for i in range(1, len(count_arr)):
        print(count_arr[i], count_arr[i-1])
        count_arr[i] += count_arr[i-1]
    # 원본 배열의 값들을 순회
    # 값들이 정렬된 인덱스 위치에 담기

    for num in numbers:
        count_arr[num] -= 1
        result[count_arr[num]] = num
        print(result)
    return result

numbers = [0, 4, 1, 3, 1, 2, 4, 1]
counting_sort(numbers, 5)