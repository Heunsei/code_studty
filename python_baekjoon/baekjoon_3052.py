# 자연수를 받아서 42로나눈 나머지를 비교하는 문제
# 한줄씩 10 번 입력값 받아오기
div_result=[]
tmp = []
for n in range(10):
    number = int(input())
    div_result.append(number % 42) 
    
for i in div_result:
    # tmp를 사용해서 tmp에 없으면 값추가
    # set으로 변경해서 unique하게 바꾸는법도 있음
    if i not in tmp:
        tmp.append(i)
print(len(tmp))

