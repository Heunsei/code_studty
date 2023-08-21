# 받아온 영어 입력값을 팰린드롬으로 만들기
# 홀수개가 여러개 있으면 못만듬
count = dict()
N = input()

for ch in N:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

# count 에 있는 value 값 중 홀수값이 2개 이상이면 못만드니까
if sum(i % 2 for i in count.values()) > 1:
    print("I'm Sorry Hansoo")
else:
    half = ''
    # 순서대로 정렬해서 출력하자
    for k, v in sorted(count.items()):
        half += k * (v//2)

    ans = half

    for k, v in count.items():
        if v % 2:
            ans += k
            break
    ans += ''.join(reversed(half))

    print(ans)

