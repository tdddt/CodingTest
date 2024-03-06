# https://level.goorm.io/exam/100821/15%ED%9A%8C-epper-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95/quiz/1

user_input = input()


# 연달아 등장하는 문자의 출현 횟수 기록. 
# 이때 출현 횟수는 알파벳으로 표현 -> 아스키 코드 활용
sol = ""

# 비트열이 0이 아니라 1로 시작하는 경우에는 맨 앞에 1붙이기
if(user_input[0]==1):
	sol += 1
	
while len(user_input)>0:
	check = user_input[0]
	count = 1
	for i in range(1,len(user_input)):
		if(user_input[i]==check):
			count +=1
		else :
			break

    # 파이썬 아스키 코드
    # ord("A") # 65
    # chr(65) # A 
	sol += chr(64+count) # chr(64+출현 횟수)로 계산
	user_input=user_input[count:]
 
print(sol)	