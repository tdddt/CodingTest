# https://school.programmers.co.kr/learn/courses/30/lessons/72416
# dp로 풀어야하는데 구현으로 삽질한 코드

# 직원 번호, 하루평균 매출액
# 모든 직원들은 다른 누군가로부터 정확히 1개의 화살표를 받음(CEO제외)
# 한 직원은 최대 2개의 팀에 소속 가능(팀장으로, 팀원으로)
# 받는 화살표o + 시작하는 화살표o -> 팀장인 동시에 팀원
# 받는 화살표o + 시작하는 화살표x -> 팀원
# 받는 화살표x + 시작하는 화살표o -> CEO
# 팀 개수 : 팀장 인원 + 1(CEO)

# 모든 팀은 최소 1명 이상의 직원을 워크숍에 참석시켜야 함
# 워크숍에 참석하는 직원들의 평균 매출액의 합이 최소
# 두 팀에 모두 속해있는 직원은 두 팀에서 모두 참석한 것으로 인정.

def solution(sales, links): #하루평균 매출액(직원번호 순), 팀장-팀원을 나타내는 2차원 배열
    noCeo = 0
    yesCeo = 0
    team = [ [] for _ in range(len(sales)+1) ]
    noCheck = [ True for _ in range(len(team))]
    yesCheck = [ True for _ in range(len(team))]
    
    for i,j in links:
        team[i].append([j,sales[j-1]])
    
    for i in range(len(noCheck)):
        if(len(team[i])==0):
            noCheck[i] = False
            yesCheck[i] = False
    
    # team[i]의 원소들을 매출액에 따라 오름차순으로 정렬
    for i in range(len(team)):
        if(noCheck[i]==True):
            team[i].sort(key=lambda x: x[1])
        
    # 팀장이 차출되지 않을 경우
    for i in range(len(team)):
        if(noCheck[i]==True): # 팀원이 있음
            for j,k in team[i]: # i팀 팀원 검사
                if(noCheck[j]==True): 
                    # min(각 팀의 최소 팀원들의 합 OR 공통팀원)
                    noCeo += min(team[i][0][1]+team[j][0][1], sales[j-1])
                    noCheck[i] = False
                    noCheck[j] = False
                elif(len(team[i])==1): # 팀원이 모두 false일 경우, min(팀장, 최소팀원)
                    noCeo += min(team[i][0][1],sales[i-1])
    
    # 팀장이 차출될 경우
    for i in range(len(team)):
        if(i==1):
            yesCeo+=sales[0]
            yesCheck[i] = False
        if(yesCheck[i]==True): # 팀원이 있음
            for j,k in team[i]: # i팀 팀원 검사
                if(yesCheck[j]==True): # 겹치는 팀원이 있는지 검사 
                    # -> !트리구조+아래 리프노드가 어떻게 될 지 모르니까 전부 순회해봐야 하긴 함.. dpㄱㄱ
                    # min(각 팀의 최소 팀원들의 합 OR 공통팀원)
                    yesCeo += min(team[i][0][1]+team[j][0][1], sales[j-1])
                    yesCheck[i] = False
                    yesCheck[j] = False
                elif(len(team[i])==1): # 팀원이 모두 false일 경우, min(팀장, 최소팀원)
                    yesCeo += min(sales[j-1],sales[i-1])
                    
                    
    return min(yesCeo,noCeo) # 최소화된 매출액의 합