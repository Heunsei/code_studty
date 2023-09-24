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
for i in range(N//2):~~~~
    s_list[i], s_list[N-1-i] == s_list[N-1-i], s_list[i]   
print(''.join(s_list))
print(s)
```
### 패턴매칭
- 고지식한 패턴 검색 알고리즘
- 카프-라빈 알고리즘
- KMP 알고리즘
- 보이어-무어 알고리즘

1. 고지식한 알고리즘
- 부르드포스 알고리즘, 다 때려박기
```python
def bruthForce(p,t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i -j
            j = -1
        i = i + 1
        j = j + 1
    if j == M:
        return i-M
    else : return -1
```
2. KMP 알고리즘
- 문자열을 검색을 매우 빠르게 하는법
- 패턴이 어디에 등장하는지 찾아줌
- 파이배열 > [ababbab]
- 문자열을 인덱스로 나눠서 i번째 까지 나온 부분문자열에서 앞이랑 뒤랑 같은 길이가 몇인지 확인
- 위의 부분 문자열
- [a][ab] > 0, [aba] > 1(a,a 길이1)
- [abab] >2 (앞에ab,끝에ab반복) [ababb] > 0 [ababba] > 1(a,a) 
- [ababbab] > 앞의 ab 뒤에 ab 반복
```python
def kmp(all_string, pattern):
    #kmp_table
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1,len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = tabel[i-1]
        if pattern[i] == all_string[j]:
            i += 1
            table[j] = i
    # kmp
    result = []
    i = 0
    for j in range(len(all_string)):
        while i > 0 and pattern[i] != all_string_[j]:
            i = table[i-1]
        if pattern[i] == all_string[j]:
            i += 1
            if i == len(pattern):
                result.append(j - i + 1)
                i = table[i-1]
    return result
```