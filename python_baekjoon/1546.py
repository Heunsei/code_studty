# 점수중 최대 값을 M으로 설정
# 모든 점수를 점수 / M * 100으로 설정
# 시험본 과목 개수 N개를 첫줄에 입력
# 출력은 과목들의 새로운 평균

num_of_score = int(input())

scores = []
# 입력값을 ' '로 구분해서 int형식으로 변환 후 리스트 형태로 반환
scores = list(map(int, input().split(' ')))

max_score = scores[0]

for num in scores:
    if max_score < num:
        max_score = num

score_sum = 0

for num in range(num_of_score):
    # round > round(number, 반올림할 자리, 음수면 1,10,100의 자리에서 반올림)
    scores[num] =round((float(scores[num]) / max_score) * 100,2)    
    score_sum += scores[num]

print(score_sum / num_of_score)