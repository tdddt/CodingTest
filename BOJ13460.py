# https://www.acmicpc.net/problem/13460
# 보드 세로(N) x 가로(M)

# 좌/우/상/하 기울이기
def move(direction):
    global Red,Blue,RedTF,BlueTF,board
    if(direction=='L'):
        # R,B가 왼쪽 #에 닿을 때까지 이동(행 판별)
        # Red[0], Blue[0] 판단
        # Red[1]의 왼쪽 하나씩 판단해서 #, B 이 있는 바로 앞으로 R위치 변경
        for i in range(Red[1],-1,-1):
            if(board[Red[0]][i]=='#' or board[Red[0]][1]=='B'):
                board[Red[0]][Red[1]]='.'
                Red = [Red[0],i+1]
                board[Red[0]][Red[1]]='R'
            # 중간에 O있으면 통과
            if(board[Red[0]][i]=='O') : 
                RedTF = True
                
        # Blue[1]의 왼쪽 하나씩 판단해서 #, R이 있는 바로 앞으로 B위치 변경                
        for i in range(Blue[1],-1,-1):
            if(board[Blue[0]][i]=='#' or board[Blue[0]][1]=='B'):
                board[Blue[0]][Blue[1]]='.'
                Blue = [Blue[0],i+1]
                board[Blue[0]][Blue[1]]='B'
            # 중간에 O있으면 통과
            if(board[Blue[0]][i]=='O') : 
                BlueTF = True
            
    elif(direction=='R'):
        # R,B가 오른쪽 #에 닿을 때까지 이동(행 판별)
        # Red[0], Blue[0] 판단
        for i in range(Red[1],M):
            if(board[Red[0]][i]=='#' or board[Red[0]][1]=='B'):
                board[Red[0]][Red[1]]='.'
                Red = [Red[0],i-1]
                board[Red[0]][Red[1]]='R'
            # 중간에 O있으면 통과
            if(board[Red[0]][i]=='O') : 
                RedTF = True
                
        for i in range(Blue[1],M):
            if(board[Blue[0]][i]=='#' or board[Blue[0]][1]=='B'):
                board[Blue[0]][Blue[1]]='.'
                Blue = [Blue[0],i-1]
                board[Blue[0]][Blue[1]]='B'
            # 중간에 O있으면 통과
            if(board[Blue[0]][i]=='O') : 
                BlueTF = True
                
    elif(direction=='U'):
        # R,B가 위쪽 #에 닿을 때까지 이동(열 판별)
        # Red[1], Blue[1] 판단
        for i in range(Red[0],-1,-1):
            if(board[i][Red[1]]=='#' or board[i][Red[1]]=='B'):
                board[Red[0]][Red[1]]='.'
                Red = [i+1,Red[1]]
                board[Red[0]][Red[1]]='R'
            # 중간에 O있으면 통과
            if(board[i][Red[1]]=='O') : 
                RedTF = True
        
        for i in range(Blue[0],-1,-1):
            if(board[i][Blue[1]]=='#' or board[i][Blue[1]]=='B'):
                board[Blue[0]][Blue[1]]='.'
                Blue = [i+1,Blue[1]]
                board[Blue[0]][Blue[1]]='B'
            # 중간에 O있으면 통과
            if(board[i][Blue[1]]=='O') : 
                BlueTF = True
        
    elif(direction=='D'):
        # R,B가 아래쪽 #에 닿을 때까지 이동(열 판별)
        # Red[1], Blue[1] 판단
        for i in range(Red[0],N):
            if(board[i][Red[1]]=='#' or board[i][Red[1]]=='B'):
                board[Red[0]][Red[1]]='.'
                Red = [i-1,Red[1]]
                board[Red[0]][Red[1]]='R'
            # 중간에 O있으면 통과
            if(board[i][Red[1]]=='O') : 
                RedTF = True
                
        for i in range(Blue[0],N):
            if(board[i][Blue[1]]=='#' or board[i][Blue[1]]=='B'):
                board[Blue[0]][Blue[1]]='.'
                Blue = [i-1,Blue[1]]
                board[Blue[0]][Blue[1]]='B'
            # 중간에 O있으면 통과
            if(board[i][Blue[1]]=='O') : 
                BlueTF = True

N, M = map(int, input().split())

# input
board = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    board[i] = list(input())
    
# 공 통과 여부
RedTF = False
BlueTF = False

# Red, Blue 위치 찾기
Red = [0,0]
Blue = [0,0]
for i in range(N):
    for j in range(M):
        if(board[i][j]=='R'):
            Red = [i,j]
        if(board[i][j]=='B'):
            Blue = [i,j]

# count = 0 ? => 방문체크나 ... 아니면 dp로 기록해야할 거 같은데 흠
            
# print("RED:",Red)
# print("BLUE:",Blue)
# for i in range(N):
#     print(board[i])
    
count = 0 # 최적의 move 찾기 (최소 횟수 파악)

while(RedTF==False and BlueTF == False):
    # 상하좌우 탐색(move)?
    
    count+=1
    if(count>10 or BlueTF==True):
        print(-1)
    if(RedTF==True and BlueTF==False):
        print(count)