# https://www.acmicpc.net/problem/16928

# 내가 원하는 수로 주사위 조작 -> 최소 몇 번만에 도착 가능?

# 10*10 보드판 -> 1차원으로 풀어야 함
# board = [[0 for _ in range(10)] for _ in range(10)]

# cnt = 1
# for i in range(10): # 0~9
#     for j in range(10): #0~9
#         board[i][j] = cnt
#         cnt+=1
# print(board)

# 주사위를 굴려 나온 수를 더한 칸의 숫자로 이동
# 100을 넘어가면 이동x
# 도착 칸이 사다리면 사다리를 타고 위로 올라감 -> 아래로 내려간다고 보고 보드판 만듦,,,
# 도착 칸이 뱀이라면 뱀을 타고 아래로 내려감 -> 위로 올라간다고 보고 보드판 만듦,, ㅎㅎ

# 1번 칸 시작 -> 목표 : 100번 칸 도착 
from collections import deque

board = [i for i in range(101)] # 0~100

# visited = [False]*101
visited = [0] * 101 # 여기까지 오는데 굴린 주사위 횟수 저장

# N : 사다리의 수, M : 뱀의 수
N,M = map(int,input().split())

# list가 아니라 dict로 받기
# ladder = dict()
# snake = dict()

for i in range(N):
    # x칸 도착 시, y칸으로 이동
    x,y = map(int,input().split())
    board[x] = y
    
for i in range(M):
    # u칸 도착 시, v칸으로 이동
    u,v = map(int,input().split())
    board[u] = v

# 1~6의 범위 중 최대 경우의 수.. -> dfs인가?
# 주사위를 최소 몇 번 굴려야 하는지 !!
def bfs(locate):
    q = deque([locate])
    
    while q:
        now = q.popleft()
        
        for i in range(1,7): # 주사위 1~6
            if(now+i>100): # 100보다 크면 판 벗어남
                continue
            
            next = board[now+i] # 이동 위치 저장
            
            if visited[next] == 0: # 처음 도착한 곳이라면
                visited[next] = visited[now]+1 # 이전 횟수 +1
                q.append(next) # 다음 위치 저장 ㄱ
                
                if next == 100:
                    return visited[100]
            
    return False
                
print(bfs(1))                