# https://www.acmicpc.net/problem/1404

# 8명이 참가하는 스타크래프트 토너먼트
# 3개의 라운드
# 1번 라운드 : i번 경기는 2xi번 참가자와 2xi+1번 참가자의 경기 (0<=i<=3), 4명의 승자가 라운드 2로 진출
# 2번 라운드 : 2xi번 경기의 승자, 2xi+1번 경기의 승자가 서로 경기 (0<=i<=1), 2명의 승자가 라운드 3에 진출
# 3번 라운드 : 승자가 토너먼트의 승자를 가리기 위해서 한 게임

# 8명의 참가자가 서로와 싸웠을 때 이길 수 있는 승률이 input
# 각 참가자가 우승할 수 있는 확률 구하기

# 28개 : 7 - 6 - 5 - 4 - 3 - 2 - 1
# => 8*8 맵으로 나눠야 할 듯? 
# win[x][y] = x와 y가 싸웠을 때, x가 이길 확률
prob = list(map(int,input().split())) # 0~100 사이의 정수
win = [[0.0 for _ in range(8)] for _ in range(8)]

idx=0
# prob을 win에 집어넣기
for i in range(8):
    for j in range(i+1,8):
        win[i][j] = prob[idx] / 100
        win[j][i] = 1-win[i][j]
        idx+=1
        
ans = [0.0 for _ in range(8)]

# 각 참가자가 우승할 수 있는 확률은 어떻게 구하지 흠

# 라운드 1 : (0,1)(2,3)(4,5)(6,7)
win_1 = [0.0 for _ in range(8)] # 라운드1에서 우승할 확률
for i in range(0,8,2):
    win_1[i] = win[i][i+1]
    win_1[i+1] = win[i+1][i]
    
# 라운드 2 : (0,1vs2,3)(4,5vs6,7)
win_2 = [0.0 for _ in range(8)] 
# 라운드2에서 우승할 확률 : 1에서 우승할 확률 * 상대팀 우승자가 1에서 우승할 확률 * 붙었을 때 이길확률
for i in range(0,8,4): # (0~3)
    for j in range(i,i+2): # 0,1 둘 중 한 명이 우승할 경우
        for k in range(i+2,i+4): # 2,3 둘 중 한 명이 우승할 경우
            win_2[j] += win_1[j]*win_1[k]*win[j][k]
            win_2[k] += win_1[k]*win_1[j]*win[k][j]
    
# 라운드 3 : (0~3vs4~7)
for i in range(4): # (0~3)
    for j in range(4,8): # vs (4~7)
        ans[i] += win_2[i]*win_2[j]*win[i][j]
        ans[j] += win_2[j]*win_2[i]*win[j][i]

for i in ans: # 소숫점 9자리까지 출력
    print(f"{i:.9f}", end=' ')