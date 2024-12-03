# DFS
def dfs(arr, start, visited):
    visited[start] = True
    for i in arr[start]:
        if(visited[i]==False):
            dfs(arr,i,visited)

dfs(arr,0,visited)

# BFS
from collections import deque
def bfs(arr,start,visited):
    visited[start]=True
    q = deque([start])
    while q :
        now = q.popleft()
        for i in arr[now]:
            if(visited[i]==False):
                visited[i]=True
                q.append(i)

bfs(arr,0,visited)

# binary search
def binary(start, end, target, arr):
    while(start<=end):
        mid = (start+end)/2
        if(arr[mid]==target): return mid
        elif(arr[mid]>target): end = mid-1
        else: start = mid+1
    return None

# dp
n=99
dp = [0]*100
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])

# dijkstra
import heapq
INF = int(1e9)
V,E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
smallest = [INF]*(V+1)

smallest[start] = 0
q = []
heapq.heappush(q,(0,start))

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append(c,b)

while q :
    dist, now = heapq.heappop(q)
    if(smallest[now]<dist): continue
    for c,b in graph[now]:
        cost = dist+c
        if(cost<smallest[b]):
            smallest[b]=cost
            heapq.heappush(q,(cost,b))
            
# 플로이드 워셜
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

# 유니온-파인드
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
    
# 크루스칼 : 최소신장트리
edges = []
total = 0 

for _ in range(v):
    a,b,c = map(int,input().split())
    edges.append(c,a,b)
    
edges.sort()

for edge in edges:
    c,a,b = edge
    if(find(a)!=find(b)):
        total+=c
        union(parent,a,b)
        
# 위상정렬 : 순서대로 나열하기
V,E = map(int,input().split())
indegree = [0]*(V+1)
graph = [[]for _ in range(V+1)]

for _ in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1
    
from collections import deque

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
    print(False)
else:
    print(result)
    
    
# 다익스트라
import heapq
INF = int(1e9)
V,E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
smallest = [INF]*(V+1)

smallest[start] = 0
q = []
heapq.append(q,(0,start))

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append(c,b)
    
while q:
    dist,now = heapq.popleft(q)
    if smallest[now]<dist: continue
    for c,b in graph[b]:
        cost = dist+c
        if(cost<smallest[b]):
            cost = smallest[b]
            heapq.heappush(q,(cost,b))
            
# 크루스칼
edges = []
total = 0

for _ in range(E):
    a,b,c = map(int,input().split())
    edges.apend(c,a,b)
    
edges.sort()

for edge in edges:
    c,a,b=edge
    if(find(a)!=find(b)):
        union(a,b)
        total+=c
        
# 냅색 : 담을 수 있는 무게가 정해져 있을 때, 가치 합이 최대인 조합
n,k = map(int,input().split())
lst = [[0,0]]

for _ in range(n):
    lst.append(list(map(int,input().split())))
    
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w = lst[i][0]
    v = lst[i][1]
    for j in range(1,k+1):
        if j<w: # 가방에 넣을 수 없을 때
            dp[i][j] = dp[i-1][j]
        else: # 가방에 넣을 수 있을 때
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[n][k])

# 퇴사2 :
n = int(input())
li = [list(map(int,input().split())) for _ in range(n)] # 걸리는 시간, 가치
dp = [0]*(n+1)
maxi = 0

for i in range(n):
    maxi = max(maxi,dp[i])
    done = i+li[i][0]
    if done<=n:
        dp[done] = max(maxi+li[i][1],dp[done])
print(max(dp))