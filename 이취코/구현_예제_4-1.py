# 상하좌우

# NxN 크기의 정사각형 공간
# 왼쪽 위(1,1), 오른쪽 아래(N,N)
# LRUD
# NxN을 벗어나는 움직임은 무시
# 최종 열의 위치 반환
N = int(input())
plan = list(input().split())
x = 1
y = 1

# L R U D : 0,1,2,3
idx = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# idx 신경쓰기
for i in range(len(plan)):
    if(plan[i]=='L'):
        idx = 0
    elif(plan[i]=='R'):
        idx = 1
    elif(plan[i]=='U'):
        idx = 2
    elif(plan[i]=='D'):
        idx = 3
    nx = x+dx[idx]
    ny = y+dy[idx]
    # 범위 벗어나면 continue
    if(nx<1 or nx>N or ny<1 or ny>N):
        continue
    # 아니라면
    (x,y)=(nx,ny)

print(x,y)