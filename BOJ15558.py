# https://www.acmicpc.net/problem/15558

# 지도는 총 2개의 줄
# 각 줄은 N개의 칸(1~N)
# 위험한 칸 / 안전한 칸

# N번 칸보다 더 큰 간으로 이동하면 게임 클리어
# 한 칸 앞 = i+1, 한 칸 뒤 = i-1, 반대편 점프 = i+k칸이동
# 1초에 한 번씩 각 줄의 첫칸이 사라짐
# 0 = 위험한 칸, 1 = 안전한 칸

# 게임 클리어 여부 구하기
N,K = map(int,input().split())
left = list(map(int,input())) # 왼쪽 줄의 0번칸에서 시작
right = list(map(int,input())) # N-1보다 크면 게임 클리어
graph = [left+[1]*K,right+[1]*K] # 뒤에 K개 추가...
# 게임 시작 0초
# 유저 움직이고 +t초, t번칸 이전은 위험한 칸으로 변함

# 그래프 .. [0][N]이나 [1][N]에 도착할 수 있으면 됨
from collections import deque

# bfs : 큐
# 1. 최상위 노드 삽입, True 처리
# 2. 인접 노드 전부 삽입, False 처리
visited = [[False]*(N+K) for _ in range(2)]
q = deque([(0,0,-1)]) # x,y,d
visited[0][0] = True

while q:
    x,y,d = q.popleft()
    if(d>=y): # 시간이 지나서 없어지는 땅 밟음 -> 고려X
        continue # 여기에서 print(0)하면 안 됨 .. 다른 경우의 수에서 도달할 수 있기 때문
    if(y>=N): # N넘어갔으니까 통과
        print(1)
        break
    
    # y-1, y+1, [!x][y+k]로 갈 수 있음
    for j in [-1,1]:
        next = y+j
        if(next>=0 and graph[x][next]==1 and visited[x][next]==False):
            visited[x][next]=True
            q.append((x,next,d+1))            
    if(graph[not x][y+K]==1 and visited[not x][y+K]==False):
        visited[not x][y+K]=True
        q.append((not x, y+K, d+1))
else: 
    print(0)