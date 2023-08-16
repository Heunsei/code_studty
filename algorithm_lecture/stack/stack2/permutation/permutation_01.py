# 순열, 내가 가진 수로 만들 수 있는 경우의 수

def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N):  # 자신으로부터 오른쪽 끝까지만 자리바꿈
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]



A = [1, 2, 3]
f(0, 3)