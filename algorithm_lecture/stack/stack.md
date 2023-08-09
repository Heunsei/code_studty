# 스택
- 스택의 특성
- 결국은 리스트로씀
1. 물건을 쌓아 올리듯 자료를 쌓아올린 자료구조
2. 선형구조
3. **후입선출(LIFO)** 
4. 마지막 원소가 top 이라 불림
- 연산
1. 삽입 > push
2. 삭제 > pop
3. isEmpty
4. peek

# 재귀 함수
```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```