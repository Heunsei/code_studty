# 접근법은 맞았으나 세부 구현 실패
import sys

N, K = map(int, sys.stdin.readline().split())
word_list = []
set_word = []

for i in range(N):
    word_list = sys.stdin.readline().rstrip()
    set_word.append(set(list(word_list)))

learn = [0] * 26

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

answer = 0

def dfs(idx, cnt):
    global answer

    if cnt == K - 5:
        readcnt = 0
        for word in set_word:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                readcnt += 1
        answer = max(answer, readcnt)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False


if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    dfs(0, 0)
    print(answer)