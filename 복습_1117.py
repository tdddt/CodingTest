# dfs
def dfs(graph, visited, start):
    visited[start]=True
    for i in graph[start]:
        if(visited[i]==False):
            dfs(graph,visited,i)
            
# bfs
from collections import deque
def bfs(graph, visited, start):
    visited[start]=True
    q = deque([start])
    while(q):
        now = q.popleft()
        for i in graph[now]:
            if(visited[i]==False):
                visited[i]==True
                q.append(i)
                
                
# binary
def binary(arr,start,end,target):
    while(start<=end):
        mid = (start+end)/2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end=mid-1
        else:
            start=mid+1

# dp
n=99
dp=[0]*100
dp[1]=1
dp[2]=1
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])

# dp1 : 냅색
n,k = map(int,input().split())
lst = [[0,0]]

for _ in range(n):
    lst.append(list(map,int,input().split()))
    
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w = lst[i][0]
    v = lst[i][1]
    for j in range(1,k+1):
        if(j<w):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[n][k])

# dp2 : 퇴사
n = int(input())
li = [list(map(int,input().split())) for _ in range(n)] # 걸리는 시간, 가치
dp = [0]*n

maxi = 0
for i in range(n):
    maxi = max(maxi,dp[i])
    done = i+li[i][0]
    if(done<=n):
        dp[done] = max(dp[done], maxi+li[i][1])
print(max(dp))

# dijkstra
import heapq
INF = int(1e9)
V,E = map(int,input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
smallest = [INF]*(V+1)

smallest[start]=0
q = []
heapq.heappush(q,(0,start))

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append(c,b)
    
while(q):
    c,b = heapq.heappop(q)
    if(smallest[b]<c):continue
    for cc,node in graph[b]:
        cost = cc+c
        if(cost<smallest[node]):
            smallest[node]=cost
            heapq.heappush(q,(cost,node))
            
# 플로이드워셜
INF = int(1e9)
V,E = map(int,input().split())
graph = [[INF]*(V+1) for _ in range(V+1)]

for a in range(1,V+1):
    for b in range(1,V+1):
        if a==b : graph[a][b] = 0
        
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1,V+1):
    for a in range(1,V+1):
        for b in range(1,V+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            
# union-find
def find(parent,x):
    if(x!=parent[x]):
        parent[x] = find(parent,parent[x])
    return x

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    
    if(a>b) : parent[a]=b
    else : parent[b]=a
    
# 크루스칼
V,E = map(int,input().split())
parent = [ i for i in range(V+1)]

edges = []
total = 0

for _ in range(E):
    a,b,c = map(int,input().split())
    edges.append(c,a,b)
    
edges.sort()

for edge in edges:
    c,a,b = edge
    if(find(a)!=find(b)):
        total+=c
        union(parent,a,b)
            
            
# 위상정렬
from collections import deque
V,E = map(int,input().split())
indegress= [0]*(V+1)
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a,b = map(int,input().split())    
    graph[a].append(b)
    indegress[b]+=1

result = []
q = deque()

for i in range(1,V+1):
    if(indegress[i]==0):
        q.append(i)
        
while(q):
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegress[i]-=1
        if(indegress[i]==0):
            q.append(i)

if(len(result)!=V): print(-1)
else: print(result)
