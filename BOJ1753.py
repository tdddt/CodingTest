# https://www.acmicpc.net/problem/1753
# 주어진 시작점에서 다른 모든 정점으로의 최단 경로 구하기 -> 디익스트라
import heapq
import sys
input = sys.stdin.readline # 시간초과 때문에 추가함

INF = int(1e9)
V,E = map(int,input().split())
K = int(input()) # 시작정점
graph = [[] for _ in range(V+1)]
smallest = [INF]*(V+1)

# 간선 저장
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) #u-v:가중치 w

# 시작 정점 초기화
q = []
smallest[K]=0
heapq.heappush(q,(0,K))

while q:
    dist, node = heapq.heappop(q)
    if(dist>smallest[node]):
        continue
    for near_node, near_value in graph[node]:
        cost = dist+near_value
        if(cost<smallest[near_node]):
            smallest[near_node] = cost
            heapq.heappush(q,(cost,near_node))
            
for i in range(1,V+1):
    if(smallest[i]==INF):
        print("INF")
    else:
        print(smallest[i])