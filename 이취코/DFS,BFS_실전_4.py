# 미로 탈출

# NxM 크기의 직사각형 형태의 미로
# 현재 위치 (1,1) / 출구 (N,M) => (0,0) / (N-1)(M-1)
# 괴물이 있는 부분은 0, 없는 부분은 1

# 탈출하기 위해 움직여야 하는 최소 칸의 개수(첫칸,출구칸 포함)
N,M = map(int,input().split())
miro = [list(input()) for _ in range(N)]
depth = [[0]*(M) for _ in range(N)] # depth 0 : 방문X

# 최소 칸의 개수를 어떻게 구하지? depth 계산?

# dfs의 경우 : 상하좌우 -> 좌우상하로 바꾸면 에러남 ㅜㅜ
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, d):  
    depth[x][y] = d  
    if(x==(N-1) and y==(M-1)): # 가장 먼저 출구에 도달했을 때
        return True # depth 출력
    
    # 상하좌우 확인
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if(nx<0 or nx>=N or ny<0 or ny>=M):
            continue
        if(miro[nx][ny]=='1' and depth[nx][ny]==0):
            dfs(nx,ny,d+1)

# 정답 코드보고 수정
from collections import deque   
def bfs(x,y,d):
    queue = deque([(x,y)])
    depth[x][y] = d
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx<0 or nx>=N or ny<0 or ny>=M):
                continue
            if(miro[nx][ny]=='1' and depth[nx][ny]==0):
                queue.append((nx,ny))
                depth[nx][ny]=depth[x][y]+1
    
# dfs(0,0,1)
bfs(0,0,1)
print(depth)
print(depth[N-1][M-1])
