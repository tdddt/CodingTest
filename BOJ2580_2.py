# https://www.acmicpc.net/problem/2580

map = [list(map(int,input().split())) for _ in range(9)]

square = [[[[True] for _ in range(10)] for _ in range(3)] for _ in range(3)]
row = [[True for _ in range(10)] for _ in range(9)]
col = [[True for _ in range(10)] for _ in range(9)]

zero = []
def dfs(cnt):
    if(cnt==len(zero)):
        # 결과 출력
        for i in range(9):
            print(*map[i])
        exit()
    x,y = zero[cnt]
    for i in range(1,10):
        if(row[x][i] and col[y][i] and square[x//3][y//3][i]):
            map[x][y] = i
            row[x][i] = False
            col[y][i] = False
            square[x//3][y//3][i] = False
            
            dfs(cnt+1)

            row[x][i] = True
            col[y][i] = True
            square[x//3][y//3][i] = True
            map[x][y] = 0
    

for i in range(9):
    for j in range(9):
        num = map[i][j]
        if(num==0):
            zero.append([i,j])
        else:
            row[i][num] = False
            col[j][num] = False
            square[i//3][j//3][num] = False
        
dfs(0)
