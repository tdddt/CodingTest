# https://www.acmicpc.net/problem/25206

# 전공평점 계산 = (학점*과목평점)합/학점합

grade = {'A+':4.5,'A0':4.0, 'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
# P인 과목은 계산에서 제외

sub = [ list(input().split()) for _ in range(20)]

mul = 0
all_credit = 0
for name, credit, score in sub:
    if(score!='P'):
        all_credit += float(credit)
        mul += float(credit)*grade[score]
print(mul/all_credit)