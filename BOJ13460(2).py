from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)] #방문여부
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1) # 상하좌우이동
q = deque()

# 구슬 좌표저장
def init():
    rx, ry, bx, by = [0] * 4 # 좌표초기화
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R': 
                rx, ry = i, j
            elif board[i][j] == 'B': 
                bx, by = i, j
    q.append((rx, ry, bx, by, 1)) # 현재 구슬의 위치와 depth(몇 번 돌렸는지) 파악
    visited[rx][ry][bx][by] = True
    
# 구슬 이동
def move(x, y, dx, dy):
    count = 0 # 이동한 칸 수 
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft() # 구슬 위치, depth 가져오기
        if depth > 10: # 10번 이하로 움직여서 빨간 구슬 못 빼내면 -1 출력
            break
        for i in range(len(dx)): # 상하좌우 이동 ㄱ
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i]) # RED
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i]) # BLUE
                        
            if board[next_bx][next_by] == 'O': # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if board[next_rx][next_ry] == 'O': # 빨간 구슬이 구멍에 떨어진다면(성공)
                print(depth) # 결과 출력
                return
            if next_rx == next_bx and next_ry == next_by : # 둘이 동시에 같은 칸에 있으면
                if r_count > b_count: # 이동 거리가 많은 구슬(더 멀리서 온 구슬)을 한칸 뒤로
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth +1))
    print(-1) # 실패 

bfs()