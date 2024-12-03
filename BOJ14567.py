# https://www.acmicpc.net/problem/14567

# 선수 과목 이수해야 과목 이수 가능
# 1. 한 학기 들을 수 있는 과목 수 제한 X
# 2. 모든 과목은 매학기 개설

N, M = map(int,input().split()) # 과목 수, 선수 조건이 수
# A가 B의 선수 과목 : A-B
indegree = [0]*(N+1) # 진입차수
graph = [[] for _ in range(N+1)] # 전출 적어두기? graph[A] = B : A를 들어야 B를 들을 수 있음
when = [1]*(N+1) # 몇 학기에 듣는지 : # 1번부터 N번 과목까지 차례대로 최소 몇 학기에 이수할 수 있는지 여부

for _ in range(M):
    a,b = map(int,input().split())
    indegree[b]+=1
    graph[a].append(b)
    
# 진입차수가 0인 애들 -> q에 넣고 하나씩 빼기
from collections import deque
result = []
q = deque([])

for i in range(1,N+1): # 선수과목 없음 -> 1학기에 다 들어서 이걸 들어야 들을 수 있는 과목 들을 수 있게 하기
    if(indegree[i]==0):
        q.append(i)
        
flag = len(q) # 현재 라운드 끝나면 다시 flag 계산

t=2 # 선수 과목이 있는 과목은 2학기부터 시작

while q: 
    now = q.popleft()
    result.append(now)
    
    flag -=1
        
    # 전출인 애들의 진입차수 -1
    for i in graph[now]:
        indegree[i]-=1
        if(indegree[i]==0):
            when[i]= t
            q.append(i)
    
    if(flag==0): # 다음 라운드 flag 계산, 다음학기니까 t+=1
        flag = len(q)
        t+=1

print(*when[1:])