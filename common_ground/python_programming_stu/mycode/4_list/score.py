#2차원 배열
#학생들 과목평균 계산


kor_score = [24, 35, 13, 43, 23]
math_score = [11, 34, 50, 29, 38]
eng_score = [29, 48, 18, 30, 38]
midterm_score = [kor_score, math_score, eng_score]
print('Whole class: ', midterm_score)

subject = ['Korean', 'math', 'English']

a, b = map(int, input().split())

for t in subject:
    if a == 0:
        t = "Korean"
    elif a == 1:
        t = "math"
    elif a == 2:
        t = "English"

print('Student no.', b+1,"s'", t, 'score is', midterm_score[a][b])




#2차문제
print()
# 학생별 과목점수 합계(=누적점수) 및 평균 구하기
# 중첩된 for 루프 안에서 학생별 과목 점수 합계를 저장
# 과목이 바뀌면 학생을 구분하는 인덱스 값 초기화
# student_score = [0, 0, 0, 0, 0]
# else:
# unpacking
# 학생별 점수 언패킹
# a, b, c, d, e = student_score
# 해서 average구하십시오
# for subject in midterm_score
# for score in subject