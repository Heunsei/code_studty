# 단어 s를 받아와 각각의 알파벳이 처음 등장하는 위치를 출력
# 없으면 -1출력

get_alpah = list(input())


alpah_list = []
for num in range(26):
    alpah_list.append(chr(97+num))

for alp in alpah_list:
    if alp in get_alpah:
        print(get_alpah.index(alp), end=' ')
    else :
        print(-1, end=' ')
    