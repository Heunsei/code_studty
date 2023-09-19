# 조합합하밯밯밯밯밯ㅂ
# nCr n개의 요소중 r개의 요소로 만들 수 있는 조합
# 조합은 1, 2랑 2, 1이 같은걸로취급할거임 ㅇㅇ
#
def combination(depth, idx):
    if depth == 2:
        print(*com_combi)
        return
    else:
        for i in range(idx,N):
            com_combi[depth] = arr[i]
            # 중복조합 할거면 i로 그냥 조합 할거면 i+1로
            combination(depth+1, i)
arr = [1, 2, 3, 4, 5]
N = len(arr)
# 완성된 조합 리스트
com_combi = [0] * N
combination(0,0)
