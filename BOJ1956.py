# https://www.acmicpc.net/problem/1956
# 최소 사이클의 도로 길이의 합
# 도로를 따라 운동하기 위한 경로
# 사이클을 찾되, 사이클을 이루는 도로의 길이의 합이 최소가 되도록
# -> MST?  사이클? 크루스칼? 

# 시간초과로 pypy로 해결 ㅜㅜ
import sys
input = sys.stdin.readline
INF = int(1e9)
V,E = map(int,input().split())
graph = [ [INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
# 자기자신 초기화 X 

# 자기 자신으로 돌아올 때 == 사이클이 있을 때
for k in range(1,V+1):
    for a in range(1,V+1):
        for b in range(1,V+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
            
# 자기 자신으로 돌아오는 경우의 최솟값
ans = INF
for i in range(1,V+1):
    if(graph[i][i]<ans):
        ans = graph[i][i]
if(ans==INF):
    print(-1)
else:
    print(ans)