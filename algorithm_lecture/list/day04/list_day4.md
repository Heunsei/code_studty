### 2차원 배열
- 부분집합을 나타내는 방법은 비트연산을 이용
- 집합의 원소가 n개일때, 공집합을 포함한 부분집함의 수는
- 2^n개, 이 개수는 원ㅅ를 부분집합에 포함시키거나 포함하지않는 2가지 경우를 모든 원소에 적용한 경우의 수와 같다

```python
list = [1, 2, 3, 4, 5]
list_len = 5
result = []
for i in range(1<<5):
    tmp = []
    for j in range(5)
        if i & (1<<j):
            tmp.append(list[j])
    result.append(tmp)
print(result)

```
### 이진검색알고리즘
- 이진검색은 정렬이 된 경우에만 사용가능
```python
# a는 검색할 배열, N은크기, key는 찾을값
def binarySearch(a,N,key):
    start = 0
    end = N -1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return true
        elif a[middle] > key :
            end = middle - 1
        else : 
            start = middle + 1
```
```python
# 배열, 시작점, 끝, 찾을값
def binarySearch2(a, low, high, key):
    if low > high :
        return False
    else :
        middle = (low+high) //2 # 중앙값 설정
        if key == a[middle]: # 검색 성공
            return True
        elif key < a[middle]:
            # key가 작으니까 끝값을 middle -1로
            return binarySearch2(a,low,middle-1,key)
        elif a[middle] < key:
            # key가 더 크니까 시작점을 중앙보다 앞으로
            return binarySearch2(a, middle + 1, high, key)
```

### 선택정렬
- 작은 값의 원소부터 차례대로 선택해서 위치 교환
```python
def selectionSort(a,N):
    # i 에서 1더한값을 j로 쓸거라 N-1까지
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            # i 다음 수들을 순회하면서 
            # 가장 작은 수를 찾기
            if a[minIdx] > a[j]:
                minIdx = j
        # 가장작은 수를 찾았으면 서로바꾸기
        # 없으면 a[i],a[i]를 바꾸는거라 현상유지
        a[i], a[minIdx] = a[minIdx], a[i]
        
```

### 셀렉션 알고리즘
- 저장되어있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는법
- 자료정렬하고, 순서에있는 원소 가져오기
```python
def select(arr,k):
    for i in range(0.k):
        minIndex = i
        for j in range i(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr[k-1]
```