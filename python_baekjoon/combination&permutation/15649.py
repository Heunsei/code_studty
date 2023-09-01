# 자연수 N과 M이 주어졌을때 길이가 M인 수열을 모두 구하는 프로그램
N, M = map(int, input().split())
s = []
def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()


