# https://level.goorm.io/exam/100834/%EC%A0%9C15%ED%9A%8C-e-pper-6-%ED%9B%84%EC%9C%84%ED%91%9C%EA%B8%B0%EB%B2%95/quiz/1

m = int(input())
cal_list = list(input().split())

sub_num = []
sub_str = []
for i in range(m):
	if(cal_list[i].isdigit()): # 숫자일 떄 
		sub_num.append(cal_list[i])
	else: # 문자일 때 
		sub_str.append(cal_list[i])

	if(len(sub_str)==(len(sub_num)-1)): # 연산자 개수 = 숫자 개수 -1 마다 계산
		while len(sub_str)>0: # 연산자 개수가 0이 될 때까지
			# sub_num은 index -2,-1값을, sub_str은 index 0값을 가져와서 계산
			
			# 숫자와 문자 연산자 계산 방법 1) 연산자를 if-elif문으로 처리
			# 숫자와 문자 연산자 계산 방법 2) 문자열 표현식을 계산하는 eval()함수 사용 
			cal_res = eval(str(sub_num.pop(-2)) + sub_str.pop(0) + str(sub_num.pop(-1)))
			
			# 결과 값을 sub_num에 추가(순서를 고려해서 맨 뒤에 추가해야 함) ex: 5 8 2 + *
			sub_num.append(int(cal_res))

print(sub_num[0])

''' 계산과정 하나하나 찍어보기
2 3 + 2 * 2 /
= (2 + 3) 2 * 2 /
= (2 + 3) * 2 2 /
= ((2 + 3) * 2) / 2

5 8 2 + * 
= 5  * (8 2 +)
sub_num = 5 8 2
sub_str = + *

9 8 / 4 - 5 * 2 + 3 *

= (9 / 8) 4 - 5 * 2 + 3 *
= ((9/8-4)) 5 * 2 + 3 *
= (((9/8-4) * 5) 2 + 3 *
= ((((9/8-4) * 5) + 2) 3 *
= ((((9/8-4) * 5) + 2) * 3

기호가 나오면, 맨 앞 숫자를 A로 잡고, 나머지는 B로 묶어버린 뒤, B 안에서 계산 반복 -> 회귀?
'''