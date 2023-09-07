T = int(input())

arr = []

def select_sort(arr):
    N = len(arr)
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
        #print(arr)

def counting_sort(arr, l):

for _ in range(T):
    arr.append(int(input()))

select_sort(arr)
for i in arr:
    print(i)
