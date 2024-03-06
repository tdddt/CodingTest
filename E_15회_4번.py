# https://level.goorm.io/exam/100819/4-100-%EB%A7%8C%EB%93%A4%EA%B8%B0/quiz/1

numbers = list(map(int,input().split()))
numbers_sum = sum(numbers)

for i in range(len(numbers)-1):
	for j in range(i+1,len(numbers)):
		sol = numbers[i] + numbers[j]
		if(numbers_sum-sol==100):
			# 변수에 값을 저장해서 numbers.remove(숫자) 형식으로 제거하는 방법도 있음
			numbers.pop(i)
			numbers.pop(j-1) # 이미 앞선 인덱스 i를 제거했으니 j-1을 제거해야 함
			break
	if(len(numbers)==7):
		break
print(*numbers) # 괄호없이 리스트 출력
	