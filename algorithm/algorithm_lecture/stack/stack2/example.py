cal = '2+3*4/5'

result = ''  # 피연산자 + 연산자
# 연산자를 모을 스택
stack = []

# 전수조사

for char in cal:
    # 정수일때
    if char not in '+-*/':
        result += char
    else:
        stack.append(char)

# 스택에 들어있는 모든 연산자들을 result 에 더해줌
while stack:
    result += stack.pop()
    
print(result, stack)