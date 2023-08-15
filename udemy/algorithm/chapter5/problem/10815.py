# 숫자 갯수 N <= 500000

def binary_search(arr, k):
    start = 0
    end = len(arr) - 1  # 2
    while start <= end:
        mid = (start + end) // 2
        #print(f'start:{start}, end : {end}, mid : {mid}')
        if arr[mid] == k:
            print('1', end=' ')
            return
        elif arr[mid] > k:
            end = mid - 1
        elif arr[mid] < k:
            start = mid + 1
    print('0', end=' ')

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
check = list(map(int, input().split()))

for i in check:
    binary_search(cards, i)

