# https://www.acmicpc.net/problem/1012

# 인접 : 상하좌우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(xx,yy):
    queue = [(xx,yy)]
    field[xx][yy] = 0
    
    while(queue):
        xx,yy = queue.pop(0)
        
        for k in range(4):
            new_x = xx+dx[k]
            new_y = yy+dy[k]
            
            # index out of range 방지
            if(new_x<0 or new_x>=M or new_y<0 or new_y>=N):
                continue
            
            if(field[new_x][new_y]==1):
                queue.append((new_x,new_y))
                field[new_x][new_y]=0
                # bfs(new_x,new_y) # Recursion error -> queue를 사용하자 !
    
T = int(input())

for i in range(T):
    # M : 가로, N : 세로, K : 배추 개수
    M,N,K = map(int,input().split())
    field = [[0 for _ in range(N) ] for _ in range(M)]
    
    #visited = [[True] * M] * N 
    
    # 필요한 최소의 배추흰지렁이 마리 수 
    worm = 0
    
    for j in range(K):
        x,y = map(int,input().split())
        field[x][y] = 1
        # visited[x][y] = False
        
    # visited가 False인 곳만 탐색해서 True로 만들기    
    for a in range(M):
        for b in range(N):
            if(field[a][b]==1):
                bfs(a,b)
                worm+=1
                
    print(worm)