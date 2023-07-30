<<<<<<< HEAD:python_baekjoon/10811.py
basket = [] 
num_of_basket, repeat = map(int, input().split(' '))

for num in range(num_of_basket):
    basket.append(num+1)

# print(basket)


for num in range(repeat):
    # 변환 시작값 끝값 받아오기
    change_str, change_end = map(int, input().split(' '))
    # tep에 basket을 뽑아와 역으로 저장
    tmp = [i for i in basket[change_str-1 : change_end]]
    tmp.reverse()
    # 바꿀 부분만 slice를 사용해 변환
    basket[change_str - 1:change_end] = tmp
    # print(basket)
    # print(tmp) 
print(*basket)
=======
# basket을 만들고 특정 범위를 역순으로
# 두개의 입력값을 받아옴
basket, repeat = map(int,input().split())

# list comprehension
# 바구니 순서별로 번호가 1부터 있으니 i+1

basket = [ i+1 for i in range(basket) ]
# repeat만큼 횟수 반복
for n in range(repeat):
    str, end = map(int,input().split())
    # basket의 일부분에 역순을 넣어줄 리스트생성
    tmp = basket[end-1:str]
    print(tmp)
    basket[str-1:end] = tmp
    print(basket)

print(basket)
>>>>>>> c0e8152087da8caf5f361c8718eab622d4f676a7:baekjoon/python_baekjoon/10811.py
