# Q1. 1부터 인자로 넘겨받은 숫자까지의 합을 구하는
# 함수 make_sum을 작성하시오.

# make_sum(10) -> 55

def make_sum(num):
    if num == 0:
        return 0
    return num + make_sum(num-1)

print(make_sum(50))