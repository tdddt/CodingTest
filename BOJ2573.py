# https://www.acmicpc.net/problem/2573

# 2차원 배열 / 양의 정수 / 빈칸 0
# 동서남북 0이 저장된 칸 개수만큼 줄어듦 (~0까지)
# 동서남북 붙어있는 칸들은 서로 연결되어 있음
# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간을 구하는 프로그램
# 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0 출력

# 시간초과코드

from collections import deque

# input
N,M = map(int,input().split())
ice = [[0 for _ in range(M)] for _ in range(N)]
nextice = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    ice[i]=list(map(int,input().split()))

# 빙산 방문 여부 dp
dp = [[False for _ in range(M)] for _ in range(N)] 

# 초기화
def initdp():
   global ice,dp
   for i in range(N):
       for j in range(M):
          if(ice[i][j]==0):
               dp[i][j]=True
          else:
               dp[i][j]=False

## 상하좌우 0개수 찾기
def find0(x,y):
    num = 0
    if (x==0 or x==N-1 or y==0 or y==M-1):
      return 0
    if (ice[x-1][y]==0): num+=1
    if (ice[x+1][y]==0): num+=1
    if (ice[x][y-1]==0): num+=1
    if (ice[x][y+1]==0): num+=1
    return num

# 다음 빙산 구하기
def next():
    global t,ice,nextice
    t+=1
    for i in range(N):
        for j in range(M):
            nextice[i][j] = ice[i][j]-find0(i,j)
            if(nextice[i][j]<0): nextice[i][j]=0
    ice = [row[:] for row in nextice]
    
### 방문 여부 True, False 판단(한 덩어리)
def howmany(x,y): # recursion error 발생
    q = deque()
    q.append((x,y))
    while q:
        sx,sy = q.popleft()
        # if 0(False), if 1(True)
        if dp[sx][sy]:continue
        dp[sx][sy]=True
        if(dp[sx-1][sy]==False): q.append((sx-1,sy))
        if(dp[sx+1][sy]==False): q.append((sx+1,sy))
        if(dp[sx][sy-1]==False): q.append((sx,sy-1))
        if(dp[sx][sy+1]==False): q.append((sx,sy+1))  

## 빙산 덩어리 개수 판단
def checknum():
    numice=0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if(dp[i][j]==False):
                if(numice>=1):
                    print(t)
                    exit() # 프로그램 종료
                howmany(i,j)
                numice+=1
    if numice==0 : # 전부 다 녹을 때까지 분리되지 않으면 0 출력
        print(0)
        exit()
                
# 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0 출력
t = 0
while(True):
    next() # 다음 빙산 구하기
    initdp()
    checknum() # 빙산 덩어리 판단
    