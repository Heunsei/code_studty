```python
def merge(arr, low, high):
    temp = []
    mid = (low + high) // 2
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1
    for k in range(low, high + 1):
        arr[k] = temp[k - low]
    return arr
def merge_sort(arr, low, high):
    if (low >= high):
        return  # base case
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    sorted_array = merge(arr, low, high)
    return sorted_array


# test code
if __name__ == "__main__":
    unsorted_array = [5, 6, 4, 0, 2, 1, 7, 3, 8]
    print(f"unsorted array :\t {unsorted_array}")
    print(f"sorted array :\t\t {merge_sort(unsorted_array, 0, 8)}")
```