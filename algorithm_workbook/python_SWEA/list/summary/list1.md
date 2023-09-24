### 배열의 필요성
- 여러개의 변수가 필요할때 다른 변수명을 이용하여 자료에 접근하는게 아니라 하나로 묶어 사용하기위해

### 버블정렬 
```python
def BubblSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```
```python
def counting(A,B,K):
    C = [0] * k+1
    
    for i in range(0,len(A)):
        # A의 i번째 원소가 몇번 나왔는지 확인 
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]
    
    for i in range(len(N)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
```