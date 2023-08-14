# 문자열로 된 계산식
- 중위 표기법 ( 스택 이용 )
- 후위 표기법

# 먼소리징

## 변환 방법
1. 입력받은 중위 표기식에서 토큰을 읽는다
2. 토큰이 피연사자면 토큰을 출력한다
3. 토큰이 연산자 일 때, 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면
스택에 push 하고 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을때 까지
   스택에서 pop 한 후 토큰의 연산자를 push.
   top 에 연산자가 없으면 push
4.  

- 숫자를먼저 출력하고 특수문자들은 스택에 넣어뒀다가 빼는 형식을 보임


# step2
- 피연산자를 만나면 스택에 push 한다
- 연산자를 만나면 필요한 만큼의 패연산자를 스택에서 pop하여 연산하고 연산결과를 다시 
스택에 push
- 수식이 끝나면 마지막을 스택을 pop 하여 출력 

```python
6528-*2/+
```
```python
stack = [0] * 100
top = -1
s = '6528-*2/+'
for x in s:
    if x not in '+-/*':
        top += 1 # push
        stack[top] = int(x)
       
    else:
        op2 = stack.[top]
        top -= 1
        op1 = stack[top]
        top -= 1
        if x == '+':        # op1 + op2
            top += 1
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2
        elif x == '/':
            top += 1
            stack[top] = op1 / op2
        elif x == '*':
            top += 1
            stack[top] = op1 * op2
```

```python
stack = [0] * 100
top = -1
icp = {'(': 3, '*':2, '/':2, '+':1, '-':1 }
isp = {'(': 0, '*':2, '/':2, '+':1, '-':1 }

fx = '6528-*2/+'
for x in fx:
    if x  not in '(+-*/)':
        susik += k 
    elif x == ')':
        while stack[top] != '(':
            susik += stack[top]

```

### 백트래킹
1. 상대 공간 트리의 깊이 우선 검색을 실시
2. 각 노드가 유망한지를 점검
3. 유망하지않다, 노드의 부모로 돌아가 검색을 계속