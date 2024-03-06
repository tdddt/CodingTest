# https://level.goorm.io/exam/100817/15%ED%9A%8C-e-pper-3%EB%B2%88/quiz/1

# N : 노트북, M : 입고날
N,M = map(int, input().split())
sol = 0 # 노트북의 재고가 0이 될 때까지 며칠이 걸리는지
day = M
while(N>0):
	day-=1
	if(day==0): # 입고날이면 노트북 +1
		N+=1
		day=M
	sol+=1 # 날짜 +1
	N-=1 # 매일 노트북 -1
print(sol)