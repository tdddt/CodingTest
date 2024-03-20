# https://www.acmicpc.net/problem/2580

# 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 3X3 정사각형 안에서도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 9X9 스도쿠, 0 : 빈 칸

def dfs2(cnt):
    if cnt == len(zero):
        # 결과 출력
        for i in range(9):
            print(*sudoku[i])
        exit()
    x,y = zero[cnt]
    for i in range(1,10): # 1~9
        if row[x][i] and col[y][i] and square[x//3][y//3][i]: # 3개의 경우에 모두 들어있지 않은 i만 저장
            sudoku[x][y] = i 
            row[x][i] = False
            col[y][i] = False
            square[x//3][y//3][i] = False
            dfs2(cnt+1)
            row[x][i] = True
            col[y][i] = True
            square[x//3][y//3][i] = True
            sudoku[x][y] = 0
            
sudoku = [list(map(int, input().split())) for _ in range(9)] # input
zero = [] # 찾아야 할 값
            
# 0에 들어갈 수 있는 값들만 True            
row = [[True for _ in range(10)] for _ in range(9)]
col = [[True for _ in range(10)] for _ in range(9)]
square = [[[True for _ in range(10)] for _ in range(3)] for _ in range(3)] # 일종의 3X3 

# 가로, 세로, 정사각형 따로 처리
for i in range(9):
    for j in range(9):
        if(sudoku[i][j]!=0):
            row[i][sudoku[i][j]] = False
            col[j][sudoku[i][j]] = False
            square[i//3][j//3][sudoku[i][j]] = False
        else:
            zero.append([i,j])
dfs2(0) 

'''시간초과 코드
def chk_row(n,x): # x 행에 n이 들어있는지 확인하는 함수
    for i in range(9):
        if sudoku[x][i] == n:
            return False
    return True        

def chk_col(n,y): # y 열에 n이 들어있는지 확인하는 함수
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True

def chk_sq(x,y,n): # 3x3에 n이 들어있는지 확인하는 함수
    for i in range(3):
        for j in range(3):
            if sudoku[x//3*3+i][y//3*3+j]==n:
                return False
    return True
            
def dfs(cnt):
    if cnt == len(zero):
        # 결과 출력
        for i in range(9):
            print(*sudoku[i])
        exit() # 종료
    x,y = zero[cnt] 
    for i in range(1,10): # 1~9
        if chk_row(i,x) and chk_col(i,y) and chk_sq(x,y,i): # 3개의 경우에 모두 들어있지 않은 i만 저장
            sudoku[x][y] = i 
            dfs(cnt+1)
            sudoku[x][y] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]
zero = [] # 찾아야 할 값
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0 :
            zero.append([i,j])
dfs(0)

'''