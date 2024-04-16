# https://www.acmicpc.net/problem/12904

# 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임
# 연산1. 문자열의 뒤에 A추가
# 연산2. 문자열을 뒤집고 뒤에 B추가

S = list(input().split())
T = list(input().split())

while(len(T)>len(S)):
    if(T[-1]=="A"): # A면 삭제
        T.pop() 
    elif(T[-1]=="B"): # B면 삭제 후 뒤집기
        T.pop() 
        T = T[::-1] # T=T[::-1]도 가능!
            
if(T==S):
    print(1)
else:
    print(0)