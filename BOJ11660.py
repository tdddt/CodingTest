# https://www.acmicpc.net/problem/11660
import sys 
input = sys.stdin.readline # 이거 안 하면 시간 초과 남 ㅠㅠㅠ

# 표의 크기 N, 합을 구해야 하는 횟수 M
N, M = map(int,input().split())

table = [list(map(int,input().split())) for _ in range(N)] # 0~N-1

# # (x1,y1)부터 (x2,y2)까지의 합 출력 -> 사각형 그리기 -> 시간 초과~
# for i in range(M):
#     sum = 0
#     x1,y1,x2,y2=quiz[i]
#     for j in range(x1-1,x2): 
#         for k in range(y1-1,y2):
#             sum+=table[j][k]
#     print(sum)

dp = [[0]*(N+1) for _ in range(N+1)] # 0~N

# 누적합 계산 -> 일반적인 방법으로 하면 안 되는건가 .. ~
for i in range(1,N+1): # 1~N
    for j in range(1,N+1):
        # dp [i][j] = dp[i][j-1]+table[i-1][j-1]
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + table[i-1][j-1]

# quiz = [list(map(int,input().split())) for _ in range(M)] # x1,y1,x2,y2
for _ in range(M) : 
    x1,y1,x2,y2 = map(int,input().split())
    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(ans)