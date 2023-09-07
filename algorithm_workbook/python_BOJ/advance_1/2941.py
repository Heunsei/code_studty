# 단어를 두개씩 갈라서 비교?
word = input()
check = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
idx = 0
#print('len :', len(word))
# 8
while idx < len(word):
    # 세글자니까 범위를 3만큼 더 줄여서 검사
    if idx <= len(word)-3:
        if word[idx] + word[idx+1] + word[idx+2] in check:
            count += 1
            idx += 3
            continue
    if idx <= len(word) - 2:
        if word[idx] + word[idx+1] in check:
            count += 1
            idx += 2
            continue
    count += 1
    idx += 1
print(count)