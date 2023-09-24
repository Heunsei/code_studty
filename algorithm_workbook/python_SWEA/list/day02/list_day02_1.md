# APS기본파트

## 카운팅 정렬
- 정수 또는 정수로 표현가능한 자료에만 사용가능
- 각 항목의 발생 횟수를 기록
1. data에서 발생회수를 세고 인덱스되는 배열에 저장
- counts = [0]*(num+1) num개만큼 0으로 채운 리스트
- for i : 1 ->4
- counts[i] += counts[i-1]
- 카운트에 i와 i이전의 값을 더한걸 i에 넣어줌
2. data의 마지막원소에 접근 (1이니까)
3. counts[1]을 하나 감소시킴
4. 누적된 값이 1이 4번째 까지는 차지하니까 temp의 4번째 칸에
1을 넣어줌
5. 반복
6. Temp에 데이터들이 순서대로 정렬
```python
A [] # 입력배열
B [] # 정렬된 배열
C [] # 카운팅 배열

    C = [0] * (k+1)
    # 인덱스 별로 값 저장
    for i in range(0,len(A)):
        C[A[i]] +=1
    # 누적시키는 과정
    for i in range(1, len(C)):
        C[i] += C[i-1]
    # 정렬
    for i in range(len(B)-1, -1,-1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
```

## 완전 검색

```python
# 3중포문
for i1 in range(1,4):
    for i2 in range(1,4):
        if i1 != i2:
            for i3 in range(1,4):
                if i3 != i1 and i3!=i2:
                    print(i1,i2,i3)
```
## 자리수 구하기
```python
num = 456789
c = [0] * 12
for i in range(6):
    c[num % 10] += 1
    num //= 10
```


## greedy serch
```python
i = 0
rti = run = 0
while i < 10:
    if c[i] >= 3 :
        c[i] -= 3
        tri += 1 
        continue
    if c[i] >= 1 and c[i+1] >=1 and c[i+2] >= 1:\
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri == 2 : print("Baby Gin")
else : print("lose")
```