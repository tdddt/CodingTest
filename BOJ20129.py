# https://www.acmicpc.net/problem/20129

# 수식은 뒤에서 앞으로 계산
# 연산자 계산 또한 뒤에서 앞으로 : 1-2 -> 2-1 = 1
# 연산자 우선순위 또한 바뀌어 있음
# 숫자와 연산자가 교대로
# 숫자 앞에 불필요한 0이 있을 수도
# 연산자는 + 0 * / 
# 나눗셈 : 두 숫자의 부호가 다르다면 나머지에 -를 붙임
add, sub, mul, div = map(int,input().split())
cal = {'+': add, '-': sub, '*': mul, '/': div} # 큰 숫자 == 우선순위 높음
cal = sorted(cal.items(),key = lambda x : x[1],reverse=True)

# 수식
question = list(input())

# 계산할 수식을 입력받음
# import re
# S = input().strip()
# 숫자와 연산자를 분리 (정규식을 사용하여 분리)
# numbers = list(map(int, re.findall(r'\d+', S)))  # 숫자의 앞에 있는 불필요한 0을 제거
# operators = re.findall(r'[+\-*/]', S)  # 연산자를 추출

from collections import deque
q = deque(question)

com = [] # 문자 구분해서 com에 넣기
num = [] # 숫자

temp = ""
while q:
    now = q.popleft()
    # now in "+-*/"
    if(now=="+" or now=="-" or now=="*" or now=="/"):
        com.append(now)
        num.append(int(temp)) # 숫자는 int 씌우면 0 사라짐
        temp=""
    else:
        temp+=now
num.append(int(temp)) # 마지막 숫자까지 삽입

for c,n in cal: # / - + *
    idx = len(com) -1 # com은 항상 num보다 한 개 작음
    while (idx>=0):
        if com[idx]==c:
            if(c=='/'):
                num[idx] = int(eval(f"{num[idx+1]}{c}{num[idx]}"))
            else:
                num[idx] = eval(f"{num[idx+1]}{c}{num[idx]}")
            num.pop(idx+1)
            com.pop(idx)
        idx-=1
print(num[0])


# 7+5-5+2*3 = 7+5-5+6 = 7+0+6 = 13
# div인 경우 com에서 /인 애들 가져오기
# /위치 i -> i+1 / i 해서 다시 i위치에 집어넣기
# num[i] = num[i+1]/num[i]
# i+1 값에 있는 애는 삭제 삭제 : num.pop(i+1)