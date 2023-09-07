# 연속된 단어 찾기
# 앞에 나왔던 단어가 떨어져서 나오면 틀린거
T = int(input())
count = 0
for i in range(T):
    tmp = []
    # 단어 받아오면서 확인
    word = input()
    # if len(word) == 1:
    #     continue

    for j in range((len(word))):
        if len(tmp) != 0:
            if word[j] != word[j-1]:
                tmp.append(word[j])
        else:
            tmp.append(word[j])
    if len(tmp) == len(set(tmp)):
        count += 1
    #print(tmp)
    #print(count)
print(count)