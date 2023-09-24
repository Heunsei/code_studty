# 배열의 길이, 찾을 배열의 길이, 이전까지 탐색했던 원소의 인덱스
def ncr(n, r, s):
    if r == 0:
        print(comb)
    else:
        # s > 어디까지 탐색했는지 넘겨주는 변수
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            ncr(n, r-1, i+1)
            # 중복 허용
            # ncr(n, r-1, i)


A = [1, 2, 3, 4, 5]
N = len(A)
R = 3
comb = [0] * R
ncr(N, R, 0)
