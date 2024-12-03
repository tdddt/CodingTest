# 음료수 얼려 먹기

# NxM 크기의 얼음틀
# 구멍이 뚫려있는 부분은 0 / 칸막이가 있는 부분은 1
# 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 -> 연결되어 있는 경우
# 생성되는 총 아이스크림의 개수 구하기

N,M = map(int,input().split())
#00110 -> string list로 입력받기 
ices = [list(input()) for _ in range(N)]

from collections import deque
# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(ices,x,y):
    queue = deque([(x,y)])
    ices[x][y] = '1'
    
    while queue:
        nx,ny = queue.popleft() 
    
        for i in range(4): # 상,하,좌우 각각 판단해서 0인 경우, 집어넣어서 1로 바꾸기
            near_x = nx+dx[i]
            near_y = ny+dy[i]
            if(near_x<0 or near_x>=N or near_y<0 or near_y>=M):
                continue
            elif(ices[near_x][near_y]=='0'): 
                queue.append((near_x,near_y))
                ices[near_x][near_y]='1'

ans = 0
for i in range(N):
    for j in range(M):
        if(ices[i][j]=='0'):
            bfs(ices,i,j)
            ans+=1

print(ans)

# input
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
# output : 8