# 대문자로만 출력할거니까 upper
# set으로 중복값 제거
word = input().upper()
set_word = list(set(word))
# 안의 단어들의 갯수를 저장
cnt = []
for i in set_word:
    cnt.append(word.count(i))


print(cnt.count(max(cnt)))
# 최대값이 두개이상 있다
# ? 출력
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    # cnt와 set_word의 원소들의 값의 순서가 같음 
    print(set_word[cnt.index(max(cnt))])