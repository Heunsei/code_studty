# 문자열을 입력받고 반복출력
repeat = int(input())

for n in range(repeat):
    # x는 반복횟수 y는 문자열
    x, y = map(str, input().split())
    # y에있는 단어를 x만큼 반복 출력
    for z in y:
        print(z*int(x), end='',)
    print()    
