def f(i, N, s):  # s는 i-1 원소까지 부분집합의 합(포함시킬 원소의 합)
    if i == N:
        print(bit, end=' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end=' ')
        print(f'.sum : {s}')
        return

    else:
        bit[i] = 1  # 부분집합의 A[i] 포함
        f(i+1, N, s+A[i])
        bit[i] = 0  # 부분집합에서 A[i] 빠짐
        f(i+1, N, s)
    return


A = [1, 2, 3]
bit = [0] * 3
f(0, 3)
