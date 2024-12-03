# https://www.acmicpc.net/problem/11437

# N개의 정점으로 이루어진 트리
# 루트는 1번
# 두 노드의 쌍 M개가 주어졌을 때, 두 노드의 가장 가까운 조상이 몇 번인지 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

import math
# 이진 상승 테이블을 위한 log 값 설정
LOG = math.ceil(math.log2(N))

# 노드 저장을 어떻게 해야 하지 .. 흠 

# 연결된 두 정점 N-1 : 부모-자식 쌍
# 1 : 2,3
# 2 : 4,5,6
# 3 : 7,8
# 4 : 9
# 5 : 11
# 7 : 13
# 6 : 2 => 2,6 ; 둘 중에 하나가 앞에 나온 숫자라면 그 아래에 붙여야 함

# LCA : least common ancestor (최소 공통 조상)

# parent = [0]*(N+1) # 각 노드의 부모 노드
parent = [[0] * (LOG + 1) for _ in range(N + 1)]
d = [0]*(N+1) # 각 노드의 깊이
visited = [False]*(N+1) # 방문 여부
graph =[[]for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b) # 2 : 4,5,6
    graph[b].append(a)

# 깊이 구하기
def dfs(x,depth):
    visited[x] = True
    d[x] = depth
    
    for node in graph[x]: #2,3
        if not visited[node]: # 방문한 노드 : 이미 들어가 있음
            parent[node] = x # parent[2] = 1
            dfs(node,depth+1)
            
dfs(1,0) # 깊이 할당, 부모 노드 연결 

M = int(input())

# 이진 상승 테이블 구성
for j in range(1, LOG + 1):
    for i in range(1, N + 1):
        parent[i][j] = parent[parent[i][j - 1]][j - 1] # i에서 2^j만큼 위에 있는 부모

def lca(a, b):
    # 깊이 맞추기
    if d[a] < d[b]:
        a, b = b, a

    # a와 b의 깊이를 맞춤
    for i in range(LOG, -1, -1):
        if d[a] - d[b] >= (1 << i):
            a = parent[a][i]

    # 공통 조상 찾음
    if a == b:
        return a

    for i in range(LOG, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

# M : 가장 가까운 공통 조상을 알고 싶은 점정 쌍
for _ in range(M):
    a,b = map(int,input().split())
    print(lca(a,b))