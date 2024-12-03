# https://www.acmicpc.net/problem/2252

# N명의 학생들을 키 순서대로 
# 두 학생의 키를 비교하여 정렬하는 방식

# 위상정렬 문제
# hint : 답이 여러 가지인 경우에는 아무거나 출력

N,M = map(int,input().split()) # 학생 수, 키를 비교한 횟수
indegree = [0]*(N+1) # 진입차수

# 간선 
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b) # a->b
    # b의 진입차수 1추가
    indegree[b] +=1
    
# 진입차수가 0인 애들 q에 넣기
from collections import deque
q = deque()
for i in range(1,N+1):
    if(indegree[i]==0):
        q.append(i)
        
result = []
# 큐가 빌때까지 반복
while q:
    now = q.popleft()
    result.append(now)
    
    # 연결된 애들 진입차수 -1
    for i in graph[now]:
        indegree[i]-=1
        # 진입차수가 0이라면 q에 넣기
        if(indegree[i]==0):
            q.append(i)

print(*result)