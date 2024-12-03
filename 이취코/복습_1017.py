# DFS : Depth, 깊이 우선 탐색, 스택, 재귀
# 1. 시작 노드 추가
# 2. 방문하지 않은 인접 노드 추가
# 3. 더 이상 방문하지 않은 인접 노드가 없다면 스택에서 꺼내서 탐색

def dfs(arr,start,visited):
    visited[start] = True
    for i in arr[start]:
        if(not visited[i]):
            dfs(arr,i,visited)
            
dfs(arr,0,visited)

# BFS : Bredth, 너비 우선 탐색, 큐
# 1. 시작 노드 추가
# 2. 방문하지 않은 인접 노드 전부 추가
# 3. 큐가 빌 때까지 반복
from collections import deque
def bfs(arr,start,visited):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in arr[now]:
            if(not visited[i]):
                visited[i]=True
                q.append(i)
                
bfs(arr,0,visited)

# DP : 다이나믹 프로그래밍
# 문제를 작게 쪼개서 쓰는 방법
# ex) 팩토리얼 문제
# 1) 탑다운 - 재귀 / 2) 바텀업 - 반복

# 탑다운
dp = [0]*100
def factorial(n):
    if n==1 or n==2:
        return 1
    # 계산한 적이 있다면 return
    if dp[n]!=0:
        return dp[n]
    dp[n] = factorial(n-1)+factorial(n-2)
    return dp[n]

# 바텀업
n=99
dp = [0]*100
dp[1]=1
dp[2]=2
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
dp[99]

# 최단경로
# 한 정점에서 다른 모든 정점까지의 최단 거리 구하기

# 다익스트라(직접 구현)
# .... 외우자 !
INF = int(1e9)
V,E = map(int,input().split())
start = int(input())
graph = [[]for _ in range(V+1)]
smallest = [INF]*(V+1)

visited = [False]*(V+1) # 방문여부

# 간선 정보

# 방문하지 않은 노드 중 최단 거리가 최소인 노드 반환
def small_n():
    min_value = INF
    idx=0
    for i in range(1,n+1):
        if(smallest[i]<INF and not visited[i]):
            min_value = smallest[i]
            idx = i
    return idx

def dijkstrat(start):
    visited[start]=True
    smallest[start]=0
    
    for j in graph[start]:
        smallest[j[0]]=j[1]
        
        
    for i in range(n-1):
        now = small_n()
        visited[now]=True
        
        for j in graph[now]:
            cost = smallest[now]+j[1]
            if(cost<smallest[j[0]]):
                smallest[j[0]]=cost
                

# 다익스트라(heapq)
import heapq
INF = int(1e9)
V,E = map(int,input().split())
start = int(input())
graph = [[]for _ in range(V+1)]
smallest = [INF]*(V+1)

# 간선 정보
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
# 초기화
smallest[start]=0
q = []
heapq.heappush(q,(0,start))

while q:
    dist, node = heapq.heappop(p)
    if(smallest[node]<dist):
        continue
    for b,c in graph[node]:
        cost = dist+c
        if(cost<smallest[b]):
            smallest[b]=cost
            heapq.heappush(q,(cost,b))


# 다익스트라 heap (try1)
import heapq
INF = int(1e9)
V,E = map(int,input().split())
start = int(input()) # 시작 정점
graph = [[] for _ in range(V+1)]
smallest = [INF]*(V+1)

# 간선입력
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    
# 초기화
smallest[start] = 0
q = []
heapq.heappush(q,(0,start))

# 최단 거리 구하기
while q:
    dist, node = heapq.heappop(q)
    if(dist>smallest[node]): # 이미 최소값이라 구할 필요X
        continue
    for d,n in graph[node]: # 인접 노드 계산
        cost = dist+d
        if(cost<smallest[n]):
            smallest[n]=cost
            heapq.heappush(q,(cost,n))

# 플로이드 워셜
INF = int(1e9)
V,E = map(int,input().split())
graph = [[INF]*(V+1) for _ in range(V+1)]
 
# 간선정보
for _ in range(E): 
    a,b,c = map(int,input().split())
    graph[a][b]=c
    
# 초기화
for a in range(1,V+1):
    for b in range(1,V+1):
        if a==b : graph[a][b]=0
        
# 알고리즘
for k in range(1,V+1):
    for a in range(1,V+1):
        for b in range(1,V+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

# 이진탐색
def binary(arr,target,start,end):
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return None


# mid로 구하기..
# 1. 재귀
def binary(arr, target, start, end):
    if(start>end):
        return
    mid = (start+end)//2
    if(arr[mid]==target):
        return mid
    elif(arr[mid]>target):
        binary(arr,target,start,end-1)
    else:
        binary(arr,target,mid+1,end)
    return None
    
# 2. 반복
def binary(arr, target, start, end):
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return None
    
# 그래프
# union-find


def find(parent,x):
    if(parent[x]!=x):
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b


N,M = map(int,input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    union(parent,a,b)



# 크루스칼 : 최소 신장 트리





# union-find : 소수점 찾기 ..
def find(parent,x):
    if(parent[x]!=parent):
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b
        ㅂ
for _ in range(N):
    a,b = map(int,input().split())
    if(find(parent,a) == find(parent,b)):
        union(parent,a,b)
        
# 크루스칼 : 최소신장트리(사이클X,모든노드포함,최소값으로)
# 어케 구하지 ..

# 위상정렬
# 까먹음 ㅜㅜ

# 정렬
# 선택정렬
