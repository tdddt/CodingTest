# https://www.acmicpc.net/problem/3085

# NxN크기에 사탕 채워넣기
# 사탕의 색이 다른 인접한 두 칸 고르고, 고른 칸에 들어있는 사탕을 서로 교환
# 같은 색으로 이루어져 있는 가장 긴 연속 부분을 고른 다음 사탕을 모두 먹음
# 먹을 수 있는 사탕의 최대 개수

N = int(input())
candy = [list(input()) for _ in range(N)]

# 일단 보드판 만들고
# 아 접근을 어떻게 해야하지
# 주변 값 탐색? 
# 일단 같은 행, 열을 탐색해야 하나?
# 주변 행,열 포함 총 몇개의 같은 색 사탕이 있는지? -> 얘네는 어차피 교환해서 가져올 수 있으니까?

# 사탕색은 4종류 : CPZY

# 인접한 두 칸이 있을 때, 서로 교환해야 함 
# 1. 인접한 칸을 교환하면서 동시에 탐색
# 2. 교환은 오른쪽 칸&아래쪽 칸만 신경쓰면 됨 
# 3. 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다

def count_candy(board, N):
    max_count = 0
    
    # 행 계산
    for i in range(N):
        count = 1
        for j in range(1,N):
            if candy[i][j]==candy[i][j-1]:
                count+=1
            else:
                max_count = max(max_count,count)
                count=1
        max_count = max(max_count, count)
        
    # 열 계산
    for i in range(N):
        count = 1
        for j in range(1,N):
            if candy[j][i]==candy[j-1][i]:
                count+=1
            else:
                max_count = max(max_count,count)
                count=1
        max_count = max(max_count, count)
        
    return max_count

max_candy = 0 
for i in range(N):
    for j in range(N):
        if j+1<N: # 오른쪽 swap
            candy[i][j], candy[i][j+1] = candy[i][j+1],candy[i][j]
            max_candy = max(max_candy, count_candy(candy,N))
            candy[i][j], candy[i][j+1] = candy[i][j+1],candy[i][j] # 원래대로
        
        if i+1<N: # 아래쪽 swap
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            max_candy = max(max_candy, count_candy(candy, N))
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j] # 원래대로
            
print(max_candy)