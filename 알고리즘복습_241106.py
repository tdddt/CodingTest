# 1. DFS,BFS
'''
DFS : 스택, 재귀
1. 시작 노드 삽입, 방문처리
2. 주변 노드 하나 삽입, 방문처리
3. 더 이상 넣을 주변 노드가 없으면, 스택 맨 위 노드 빼서 주변 노드 탐색
'''

def dfs(graph,start,visited):
    visited[start] = True
    for i in graph[start]:
        if(visited[i]==False):
            dfs(graph,i,visited)
            
dfs(graph,0,visited)
    

'''
BFS : 큐
1. 시작 노드 삽입, 방문 처리
2. 주변 노드 전부 삽입, 방문처리
'''
from collections import deque
def bfs(graph,start,visited):
    visited[start]=True
    q = deque([start])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if(visited[i]==False):
                visited[i]=True
                q.append(i)

bfs(graph,0,visited)

# 2. 이진탐색
'''
재귀
'''
def binary_recurstion(arr,target,start,end):
    if(start>end):
        return None
    mid = (start+end)/2
    if(arr[mid]==target):
        return mid
    elif(arr[mid]>target):
        binary_recurstion(arr,target,start,mid-1)
    else:
        binary_recurstion(arr,target,start+1,end)


'''
반복
'''
def binary_repeat(arr,target,start,end)
    while(start<=end):
        mid = (start+end)/2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return None

# 3. DP : 피보나치 수열
'''
탑다운, 재귀
'''
dp = [0]*100

def fibo_recursion(x):
    if x==1 or x==0:
        return 1
    if dp[x]!=0:
        return dp[x]
    dp[x] = fibo_recursion(x-1)+fibo_recursion(x-2)
    return dp[x]

'''
바텀업, 반복문
'''
n=99
dp = [0]*100
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])

# 4. 최단경로 : 다익스트라, 플로이드 워셜
'''
다익스트라 : 한 노드에서 다른 모든 노드까지의 최소 거리
1. 초기화
2. 간선 저장
3. 계산
'''
INF = int(1e9)
V,E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
smallest = [INF] * (V+1)

import heapq

smallest[start] = True
q = []
heapq.append(q,(0,start))

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append(c,b)

while q:
    dist, now = heapq.heappop(q)
    if(smallest[now]<dist):
        continue
    for c,b in graph[now]:
        cost = dist + c
        if(cost<smallest[b]):
            smallest[b]=cost
            heapq.heappush(q,(cost,b))
    

'''
플로이드 워셜 : 모든 정점에서 다른 모든 정점까지의 최소 거리
1. 초기화
2. 간선 저장
3. 계산
'''
INF = int(1e9)
V,E = map(int,input().split())
graph = [[INF]*(V+1) for _ in range(V+1)]

for a in range(1,V+1):
    for b in range(1,V+1):
        if a==b : graph[a][b]=0

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1,V+1):
    for a in range(1,V+1):
        for b in range(1,V+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

# 5. 그래프 : 유니온파인드, 크루스칼, 위상정렬
def find(parent,x):
    if(parent[x]!=x):
        parent[x]=find(parent,parent[x])
    return parent[x]

    
def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if(a>b): parent[a]=b
    else: parent[b]=a
    
n,v = map(int,input().split())
parent = [i for i in range(n+1)]

for _ in range(v):
    a,b = map(int,input().split())
    union(parent,a,b)
    
'''
크루스칼 : 최소 신장 트리(최소한의 비용으로 구성되는 모든 노드를 포함하되 사이클이 존재하지 않는 트리)
'''
edges = []
total = 0 # 가중치

for _ in range(v):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
    
edges.sort()

for edge in edges:
    c,a,b = edge
    if(find(a)!=find(b)):
        union(parent,a,b)
        total+=c
        
'''
위상정렬 : 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하기
'''
V,E = map(int,input().split()) 
indegree = [0]*(V+1) # 진입차수

graph = [[] for _ in range(V+1)] # 진출 차수
for _ in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1
    
from collections import deque

def topology():
    result = []
    q = deque()
    
    for i in range(1,V+1):
        if indegree[i]==0:
            q.append(i)
            
    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i]-=1
            if(indegree[i]==0):
                q.append(i)
                
    if(len(result)!=V):
        return -1
    return result

# 6. N으로 표현 - dp
'''
https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3
'''

# 7. 냅색 - dp
'''
배낭에 담을 수 있는 무게의 최댓값이 정해져 있을 때, 가치 합이 최대인 조합 찾기
'''
n,k = map(int,input().split())
size = [0]
value = [0]

for _ in range(n):
    s,v = map(int,input().split())
    size.append(s)
    value.append(v)
    
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    s = size[i]
    v = value[i]
    for j in range(i,k+1):
        if j<s:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-s]+v)
print(dp[n][k])


n, k = map(int, input().split())
lst=[[0, 0]]
for _ in range(n):
    lst.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = lst[i][0]
        value = lst[i][1]
        if j < weight:  # 가방에 넣을 수 없으면
            dp[i][j] = dp[i - 1][j]  # 위에 값 그대로 가져오기
        else: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
print(dp[n][k])

# 8. 퇴사2 - dp
'''
https://www.acmicpc.net/problem/15486
'''
n = int(input())
li = [list(map(int,input().split())) for _ in range(n)] # 걸리는 시간, 버는 돈
dp = [0] * (n+1)
maximum = 0

for i in range(n):
    maximum = max(maximum,dp[i])
    done = i + li[i][0]
    if done <= n :
        dp[done] = max(maximum + li[i][1], dp[done])
print(max(dp))

# 9. 3*n 타일링 - dp
'''
https://school.programmers.co.kr/learn/courses/30/lessons/12902
'''