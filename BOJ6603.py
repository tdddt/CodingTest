# https://www.acmicpc.net/problem/6603

# 1~49 중 6개의 수
# k개의 수를 골라 만든 집합 S

def dfs(res,case,idx): # 뽑은 숫자 리스트, 숫자풀, 최소 idx(얘 포함 큰 수에서 선택하기)
    if(len(res)==6): # 6개 뽑았으면 출력
        print(*res)
        return
    for idx in range(idx,len(case)): # idx = 0
        res.append(case[idx]) 
        dfs(res,case,idx+1) # case[0] 을 넣었을 떄 경우의 수 시작
        res.pop() # case[0] 을 넣지 않았을 때 경우의 수 시작
        
while(True): # 입출력 한 번에 
    # input 
    testcase = list(map(int,input().split()))
    if(len(testcase)==1): # 0이 들어오면 입력 종료
        break
    else: 
        # output
        dfs([],testcase[1:],0)
        print()
        
'''
# 조합 라이브러리 써서 풀기
import itertools

while True:
    testcase = list(map(int,input().split()))
    
    if(len(testcase)==1):
        break
    for i in itertools.combinations(testcase[1:],6):
        print(*i)
    print
'''
