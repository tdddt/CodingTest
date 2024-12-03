# DFS
def dfs(arr, start, visited):
    visited[start] = True
    for i in arr[start]:
        if(visited[i]==False):
            dfs(arr,i,visited)
            
# BFS
from collections import deque
def bfs(arr,start, visited):
    visited[start] = True
    q = deque([start])
    while(q):
        now = q.popleft()
        for i in arr[now]:
            if(visited[i]==False):
                visited[i]=True
                q.append(i)
                
# binary-search
def binary(start,end,arr,target):
    while(start<=end):
        mid = (start+end)/2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            end = mid-1
        else:
            start = mid+1
            
# dp
n = 99
dp = [0]*100
dp[1]=1
dp[2]=1
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])

# dijkstra
import heapq
INF = int(1e9)
V,E = map(int,input().split())
start = int(input)
graph = [[]for _ in range(V+1)]
smallest = [INF]*(V+1)

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append(c,b)

smallest[start] = 0
q = []
heapq.heappush(q,(0,start))
while(q):
    c,b = heapq.heappop(q)
    if(smallest[b]<c):continue
    for cc,nn in graph[b]:
        cost = cc+c
        if(cost<smallest[nn]):
            smallest[nn] = cost
            heapq.heappush(q,(cost,nn))
            
# 플로이드워셜
INF = int(1e9)
V,E = map(int,input().split())
graph = [[INF]*(V+1) for _ in range(V+1)]

for a in range(1,V+1):
    for b in range(1,V+1):
        if (a==b): graph[a][b]=0
        
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1,V+1):
    for a in range(1,V+1):
        for b in range(1,V+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            
            
