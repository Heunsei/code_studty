# 이상한 정렬
# arr을 받아와서 가장큰값을 pop(), 가장작은값을 pop
# 하는 식으로 새로운 리스트에 전달해서 리턴
# arr을 받아와서 값을 정렬하고 tmp를 반환
def change(arr):
    tmp = []
    while arr:
        m = arr[0] #max
        n = arr[0] #min
        max_idx = 0
        min_idx = 0
        print(len(arr))
        for i in range(len(arr)):
            if arr[i] > m:
                m = arr[i]
                max_idx = i
            if arr[i] < n:
                n = arr[i]
                min_idx = i
        print(f'idx_max : {max_idx} minidx = {min_idx}')
        print(tmp)
        print(arr)
        tmp.append(arr[max_idx])
        tmp.append(arr[min_idx])
        print(len(arr))
        arr.remove(m)
        arr.remove(n)
        print(tmp)
    return tmp

T = int(input())
for tc in range(1, T+1):
    test = int(input())
    test_list = list(map(int, input().split()))
    print(test_list)
    result = change(test_list)

    print(f'#{tc} ', end='')
    for i in range(10):
        print(result[i], end=' ')
    print()