# 그래프 

# union-find
# 서로소(공통 원소가 없는 두 집합) 찾기 
# union : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치기
# find : 특정 원소가 속한 집합이 어떤 집합인지 알려주는 연산

def find_parent(parent,x):
    if(parent[x]!=x):
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if(a<b):
        parent[b]=a
    else:
        parent[a]=b

n,v = map(int,input().split())
parent = [ i for i in range(n+1) ]

for _ in range(v):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
    
# 크루스칼
# 신장 트리 : 모든 노드를 포함하면서 사이클이 존재하지 않는 트리
# 최소 신장 트리 MST : 최소한의 비용으로 구성되는 신장 트리

edges = []
total = 0 # 가중치

# 1) 간선 정보 입력
for _ in range(v):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
# 2) cost로 정렬
edges.sort()
# 3) 부모가 같지 않을 때만 union, total 갱신
for edge in edges:
    c,a,b = edge
    if (find_parent(parent,a)!=find_parent(parent,b)): # cycle이 생기지 않을 경우
        union_parent(parent,a,b)
        total+=c
        
# 위상정렬
# 위상정렬 O(V+E)
# : 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
# ex) 선수과목을 고려한 학습 순서 설정 
# 진입 차수 InDegree : 특정한 노드로 들어오는 간선 개수
# 진출 차수 OutDegree : 특정한 노드에서 나가는 간선 개수

# 큐로 구현 가능
# 1) 진입차수가 0인 모든 노드를 큐에 넣는다.
# 2) 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
# 3) 새롭게 진입차수가 0이 된 노드를 큐에 넣기 반복

# 모든 요소를 방문하기 전에 큐가 빈다 == 사이클이 존재한다
# 스택을 활용한 DFS로도 구현 가능

V,E = map(int,input().split())
# 진입 차수 0으로 초기화
indegree = [0]*(V+1)

# 간선 정보 입력받기
graph = [[] for _ in range(V+1)] # 따지고보면 진출 차수?
for _ in range(E):
    a,b = map(int,input().split())
    graph[a].append(b) # a에서 b로 이동해야함
    indegree[b]+=1 # 진입차수 1 추가

from collections import deque
def topology():
    result = [] # 수행결과 
    q = deque()
    
    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1,V+1):
        if indegree[i]==0:
            q.append(i)
            
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        
        # 연결된 노드들의 진입차수 1빼기
        for i in graph[now]:
            indegree[i] -=1
            # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i]==0:
                q.append(i)
                
    # 수행결과 
    # 만약 모든 노드를 방문하지 않았다면(result가 길이와 다르다면) 사이클 존재 
    if len(result) != V:
        return -1
    return result

topology()