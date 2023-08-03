# 페이지 p에 대해 page를 찾을때 까지 횟수를 반환
def compare(arr, N, page):
    count = 0
    start = 0
    end = N-1
    while start <= end:
        mid = int((start + end)/2)
        if arr[mid] == page:
            count += 1
            return count
        elif arr[mid] > page:
            end = mid 
            count += 1
        elif arr[mid] < page:
            start = mid 
            count +=1

T = int(input())
for tc in range(1,T+1):


    P, Pa, Pb = list(map(int,input().split()))
    arr = [i for i in range(1,P+1)]
    N = len(arr)

    #print(compare(arr, N, Pa))
    #print(compare(arr, N, Pb))

    if compare(arr, N, Pa) > compare(arr, N, Pb):
        print(f'#{tc} B')
    elif compare(arr, N, Pa) < compare(arr, N, Pb):
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0') 

