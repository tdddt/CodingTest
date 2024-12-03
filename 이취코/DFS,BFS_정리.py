# DFS : 깊이 우선 탐색, 스택, 재귀
# 1. 탐색시작노드 삽입, 방문처리
# 2. 최상단 노드의 인접 노드 확인
# 3. 방문하지 않은 인접노드 삽입, 방문처리
# 4. 인접노드가 모두 방문했을 때, 최상단 노드 pop

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    
    # 노드 방문 순서 확인
    print(v,end=' ')
    
    # 인접 노드 확인
    for i in graph[v]:
        if(not visited[i]): # 방문하지 않은 경우, 재귀적으로 방문
            dfs(graph,i,visited)
            

# BFS : 너비 우선 탐색, 큐
# 1. 탐색시작노드 삽입, 방문처리
# 2. 최하단 노드 pop, 방문하지 않은 인접노드 전부 삽입, 방문처리
from collections import deque
def bfs(graph, start, visited):
    # 큐 생성
    queue = deque([start])
    
    # 현재 노드 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft() # 최하단 노드 pop
        for i in graph[v]: # 방문하지 않은 인접노드
            if(not visited[i]):
                queue.append(i) # 전부 삽입
                visited[i] = True # 방문 처리


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
dfs(graph,1,visited)


## 복습
# DFS : 깊이 우선, 재귀, 스택
def dfs(arr,v,visited):
    # 1) 첫번째 노드 삽입하고 체크 처리
    visited[v] = True
    # 2) 인접 노드 중 하나 방문하고 처리
    for i in arr[v]:
        if(not visited[i]):
            dfs(arr,i,visited)

# BFS : 너비 우선, 큐
from collections import deque
def bfs(arr,v,visited):
    # 1) 시작 노드 삽입하고 체크 처리
    visited[v] = True
    queue = deque([v])
    # 2) queue가 빌 때까지 반복
    while queue:
        now = queue.popleft()
        for i in arr[now]:
            if(not visited[i]):
                visited[i]=True
                queue.append(i)