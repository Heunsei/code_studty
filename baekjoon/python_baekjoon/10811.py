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