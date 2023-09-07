# 너의 평점은
# 평점 구하는문제
# 전공평점은 과목별 학점 x 과목평점을 학점의 총합으로 나눈값
# 패논패 과목은 p면 계산제외, F면 평점 0
count = 0
tmp = 0
grade_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5,
             'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
for tc in range(20):
    a, b, c = map(str, input().split())
    # tmp에 학점과 과목평점을 곱한값을 저장
    if c != 'P':
        tmp += float(b) * grade_dic[c]
        count += float(b)
print(round(tmp/count, 6))