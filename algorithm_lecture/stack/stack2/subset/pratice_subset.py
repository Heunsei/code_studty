# 1부터 10까지의 부분집합의 합을 구하기
def f(i, N, s, target):  # s는 i-1 원소까지 부분집합의 합(포함시킬 원소의 합)
    if s == target:
        print(bit)
    elif i == N:
        return
    elif s > target:
        return
    else:
        bit[i] = 1  # 부분집합의 A[i] 포함
        f(i+1, N, s+A[i], target)
        bit[i] = 0  # 부분집합에서 A[i] 빠짐
        f(i+1, N, s, target)
    return

# 부분집합의 합이 10인 경우에
N = 10
A = [i for i in range(1, 11)]
bit = [0] * N
f(0, N, 0, t)
