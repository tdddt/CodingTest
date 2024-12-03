# https://www.acmicpc.net/problem/1939

# N개의 섬으로 이루어진 나라
# 섬 사이에 설치된 다리
# 각 다리마다 중량제한 
# 한 번의 이동(섬1->섬2)에서 옮길 수 있는 물품들의 중량의 최댓값 구하기

from collections import deque

N,M = map(int,input().split()) # N: 섬, M: 다리

bridge = [[]for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    bridge[a].append([b,c])
    bridge[b].append([a,c])
    
i1, i2 = map(int,input().split()) # island1, island2

def bfs(weight):
    q = deque()
    q.append(i1)
    