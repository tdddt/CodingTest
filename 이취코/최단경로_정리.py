# 최단경로
# : 특정 지점까지 가장 빠르게 도달하는 방법을 찾는 알고리즘
# 총 3가지 : 다익스트라 / 플로이드 워셜 / 벨만 포드

# 다익스트라 최단 경로 알고리즘
# : 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로 구하기
# (음의 간선, 즉 0보다 작은 값을 가지는 간선이 없을 때만 동작 가능)
# 1) 출발 노드 설정 및 최단 거리 테이블 초기화
# 2) 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
# 3) 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블 갱신
# 4) 반복

# 파이썬에서 무한 : int(1e9)

# 구현 1: 간단한 다익스트라 알고리즘 O(V^2)
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

n,m = map(int,input().split()) # 노드, 간선
start = int(input()) # 시작 노드
graph = [[]for _ in range(n+1)] # 간선
visited = [False] * (n+1) # 노드 방문 여부
distance = [INF] * (n+1) # 최단거리 테이블

for _ in range(m): # 간선 정보
    a,b,c = map(int,input().split()) # a-b가는 길, 비용 c
    graph[a].append((b,c))
    
# 방문하지 않은 노드 중, 최단 거리가 최소인 노드 번호 반환
def get_smallest():
    min_value = INF
    idx = 0
    for i in range(1,n+1):
        if(distance[i]<INF and not visited[i]): # 최단 거리가 INF가 아니고, 방문 X
            min_value = distance[i] # 최단 거리
            idx = i
    return idx

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복
    for i in range(n-1):
        # 최단 거리가 최소인 노드 꺼내서 방문처리
        now = get_smallest()
        visited[now] = True
        # 최단 거리 테이블 갱신
        for j in graph[now]:
            cost = distance[now]+j[1]
            if(cost<distance[j[0]]):
                distance[j[0]] = cost
                
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
        
        
# 힙 자료 구조 == 우선순위 큐 : 우선순위가 가장 높은 데이터를 가장 먼저 삭제
# heapq : 첫번째 원소를 기준으로 우선순위 판단(가치, 물건) / 최소 힙(값이 낮은 데이터가 먼저 삭제)
# 최대 힙 구현 팁 : 일부러 가치에 음수부호를 붙여서 넣었다가 꺼낸 다음에 다시 양수로 만들기
     
        
# 구현2 : 개선된 다익스트라 알고리즘 O(ElogV), V노드개수 E간선개수 <- 우선순위 큐(heapq)로 최단 거리가 최소인 노드 찾기
n,m = map(int,input().split()) # 노드, 간선
start = int(input()) # 시작 노드
graph = [[]for _ in range(n+1)] # 간선
distance = [INF] * (n+1) # 최단거리 테이블

for _ in range(m): # 간선 정보
    a,b,c = map(int,input().split()) # a-b가는 길, 비용 c
    graph[a].append((b,c))

import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist: # 처리된 노드라면 무시
            continue
        for i in graph[now]: # 인접 노드 확인
            cost = dist + i[1]
            if(cost<distance[i[0]]): # 경로 갱신
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(start)

# 플로이드워셜알고리즘 O(n^3)
# : 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
# 2차원 리스트에 최단 거리 정보를 저장

INF = int(1e9)
n,m = map(int,input().split()) # 노드, 간선
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신에서 자기자신으로 가는 비용 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b: graph[a][b]=0
        
# 각 간선에 대한 정보
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
            
            
## 복습
# 플로이드 워셜 O(n^3)
INF = int(1e9)
n,m = map(int,input().split()) # 노드,간선개수
graph = [[INF]*(n+1) for _ in range(n+1)]

# 1) 자기자신 초기화
for a in range(n+1):
    for b in range(n+1):
        if (a==b): graph[a][b] = 0
        
# 2) 간선 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
# 3) 알고리즘 적용
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            
# 다익스트라 O(MlogN)
# start : 시작 노드
import heapq
INF = int(1e9)
n,m = map(int,input().split())
graph = [[]for _ in range(n+1)]
smallest = [[INF]for _ in range(n+1)]
# 1) 시작 노드 삽입
q = []
smallest[start]=0
heapq.heappush(q,(0,start))
# 2) 간선 계산
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) # 노드,가치
# 3) 다익스트라
while q:
    dist,node = heapq.heappop(q)
    if(dist>smallest[node]): # 이미 탐색한 노드라면 무시
        continue
    for b,c in graph[node]: # 주변 노드 탐색
        cost = dist+c # 비용 계산
        if(cost<smallest[b]): # 최소 비용 업데이트
            smallest[b]=cost
            heapq.heappush(q,(cost,b))
            
# 디익스트라
import heapq
n,m
start
graph = [[] for _ in range(n+1)]
smallest = [INF] * (n+1)
#1) 첫번째 원소 
q=[]
smallest[start]=0
heapq.heappush(q,(0,start))
#2)간선 저장
for _ in range(m):
    a,b,c
    graph[a].append(c,b) 
#3)계산
while q:
    dist,now = heapq.heappop(q)
    if(smallest[now]<dist): # 이미 지나갔다면
        continue
    for c,b in graph[now]: # 주위 노드 확인
        cost = dist+c
        if(cost<smallest[b]): # 최소라면
            smallest[b] = cost # 최소 업데이트
            heapq.heappush(q,(cost,b))