# https://www.acmicpc.net/problem/14238

# 3명의 직원들(A,B,C) : 하루에 한 명만 출근
# A:매일 출근 가능 / B:출근한 다음날 반드시 쉬어야 함 / C:출근한 뒤 이틀은 반드시 쉬어야 함.
# S(출근기록)가 주어졌을 때, S의 모든 순열 중 올바른 출근 기록인 것 아무거나 출력하는 프로그램
# 순열 : 중복없이 순서를 고려하여 선택하거나 나열하는 것

# 시간초과코드 -> dp를 사용해보자! 
S=list(input().strip())
worker = [0,0,0] 
L = len(S)

for i in range(L):
    worker[ord(S[i])-65] +=1

ans=['?' for _ in range(L)]
dp = [[[[[False for _ in range(3)] for _ in range(2)] for _ in range(L)] for _ in range(L)] for _ in range(L)]

def dfs(a,b,c,bb,cc): # a,b,c의 횟수 bb,cc: b와 c의 가능여부(0일 때면 일할 수 있는 상태)
    if([a,b,c]==worker):
        print(''.join(ans))
        exit(0)
    
    if(a+b+c>=L): return False # 필요한 이유 : BB 입력으로 들어왔을 때, out of range를 막기 위함
    
    if(bb<0): bb=0
    if(cc<0): cc=0
    
    if dp[a][b][c][bb][cc]: # LLL23
        return False

    dp[a][b][c][bb][cc] = True
    
    if(a>worker[0]):
        return False
    else:
        ans[a+b+c]='A'
        dfs(a+1,b,c,bb-1,cc-1)
        
    if(b>worker[1]):
        return False
    elif(bb==0):
        ans[a+b+c]='B'
        dfs(a,b+1,c,bb+1,cc-1)
        
    if(c>worker[2]):
        return False
    elif(cc==0):
        ans[a+b+c]='C'
        dfs(a,b,c+1,bb-1,cc+2)
    return False

dfs(0,0,0,0,0) 
print(-1)