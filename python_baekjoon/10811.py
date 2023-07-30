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