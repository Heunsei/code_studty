### 문자열
- 대응되는 숫자를 정해놓고 메모리에 저장
- 제공되는 문자열 클래스 함수
1. replace()
2. split()
3. isalpha()
4. find()

- 문자열 뒤집기
1. s = s[::-1]
2. s.reverse()
3. "".join(s)

```python
s = [R,e,v,e,r,s,e]
s_list = list(s)
N = len(s)
for i in range(N//2):
    s_list[i], s_list[N-1-i] == s_list[N-1-i], s_list[i]   
print(''.join(s_list))
print(s)
```
