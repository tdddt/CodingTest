# https://www.acmicpc.net/problem/23288

# 크기가 NxM지도
# 오른쪽은 동쪽, 위쪽은 북쪽
# 좌표 : (r,c) / 시작은 (1,1) 마지막은 (N,M)

# 현재 주사위 : 윗면이 1, 동쪽이 3
# 주사위가 이동 방향(초기:동쪽)으로 한 칸 굴러감.
# 이동 방향에 칸이 없으면 반대로 한 다음 한 칸 굴러감
# 도착한 칸에 대한 점수 획득
# 주사위 아랫면 정수(A)와 주사위 칸 정수(B) 비교해 이동 방향 결정
# - A>B : 동 -> 남 -> 서 -> 북
# - A<B : 동 -> 북 -> 서 -> 남
# - A==B : 변화X

# 칸에 대한 점수 = B*C
# B : (x,y)에 있는 정수
# C : (x,y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수
# -> 즉, C는 인접해서 붙어있는 B의 칸 개수

# NxM : 지도크기, K : 이동횟수
N,M,K = map(int,input().split()) 
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0

from collections import deque

def get_score(B,x,y): # bfs
    visited = [[False]*M for _ in range(N)]
    score = 0 # B*C = B + B + B + ...
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    while q:
        x,y = q.popleft()
        score += B
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if(0<=nx<N and 0<=ny<M and not visited[nx][ny]):
                if(board[nx][ny]==B):
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return score
    
# 이동방향 : 동 남 서 북 <-> 북 서 남 동
dx = [0,1,0,-1]
dy = [1,0,-1,0]

dice = [1,2,3,4,5,6]
# 동쪽으로 이동(2,5고정 & 나머지 시계방향) <-> 서쪽(나머지 반시계)
#   2       2       2    V   2
# 4 1 3   6 4 1   3 6 4  V 1 3 6
#   5       5       5    V   5
#  (6)     (3)     (1)   V   4

# 남쪽으로 이동(4,3고정 & 나머지 아래로) <-> 북쪽(나머지 위로)
#   2       6       5    V   1
# 4 1 3   4 2 3   4 6 3  V 4 5 3
#   5       1       2    V   6
#  (6)     (5)     (1)   V   2
def bottom(dir):
    global dice # 1,2,3,4,5,6
    if (dir==0): # 동 : 4,2,1,6,5,3
        dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif (dir==1): # 남 : 2,6,3,4,1,5
        dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    elif (dir==2) : # 서 : 3,2,6,1,5,4
        dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif (dir==3) : # 북 : 5,1,3,4,6,2
        dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    return dice[-1]

x,y,dir = 0,0,0 # (x,y), dir : 0~3(idx)

for _ in range(K):
    # 주사위 굴리기 (방향설정)
    next_x = x+dx[dir]
    next_y = y+dy[dir]
    
    # 이동방향에 칸이 없을 때, 반대방향으로 
    if(next_x>=N or next_x<0 or next_y>=M or next_y<0):
        # 동(0,1),idx=0 <-> 서(0,-1),idx=2
        # 남(1,0),idx=1 <-> 북(-1,0),idx=3
        next_x = x+dx[dir]*(-1)
        next_y = y+dy[dir]*(-1)
        dir = (dir+2)%4 # 방향재설정
    
    # 다음 방향 설정 (아랫면정수A, 칸정수B 비교)
    a = bottom(dir)
    b = board[next_x][next_y]
    if(a>b):
        dir = (dir+1)%4
    elif(a<b):
        dir = (dir-1)%4
    
    # 점수 계산
    ans += get_score(board[next_x][next_y],next_x,next_y)
    x,y = next_x,next_y
    
print(ans)