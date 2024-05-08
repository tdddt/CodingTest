# https://www.acmicpc.net/problem/1890

# 반드시 오른쪽이나 아래쪽으로만
# 브루트 포스? 백트래킹? - DFS?

N = int(input())
m = [list(map(int,input().split())) for _ in range(N)]

#visited = [[False for _ in range(N)]for _ in range(N)]
#visited[0][0] = True

ans = 0

# index : 0~3
def dfs(x,y):
    global ans
    if(x==(N-1) and y==(N-1)):
        ans+=1
        return
    
    if(x >= N or y >= N) : return
    dfs(x+m[x][y],y) # 오른쪽으로 가거나
    dfs(x,y+m[x][y]) # 아래쪽으로 가거나
    
dfs(0,0)
print(ans)