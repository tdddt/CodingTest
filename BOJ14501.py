# https://www.acmicpc.net/problem/14501

# N+1 퇴사, N일 동안 최대한 많은 상담
# 최대 상담 이익 구하기

# 처음에 그리디인 줄 알았는데 아님 -> 일하는 것보다 다음 일의 비용이 더 클 때 고려해야 함
# dp 문제 (bfs로도 풀 수 있음)

N = int(input())
counsel = [list(map(int,input().split())) for _ in range(N)]

dp = [0 for i in range(N+1)] # i번째 일까지 일했을 때 최대수익
for i in range(N-1,-1,-1):
    if i+counsel[i][0]>N: # 퇴사일 넘기면 상담X
        dp[i] = dp[i+1]
    else: # max(i일에 상담x, 상담o)
        dp[i] = max(dp[i+1], counsel[i][1]+dp[i+counsel[i][0]])
print(dp[0])
       