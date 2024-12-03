# https://www.acmicpc.net/problem/2225
# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램
# 덧셈의 순서가 바뀐 경우는 다른 경우로
# 한 개의 수를 여러 번 쓸 수도 있음
# 답을 1,000,000,000으로 나눈 나머지 출력

# 덧셈 경우의 수 -> 숫자 나열 경우의 수 
N, K = map(int,input().split()) #1<=N,K<=200
dp = [[0]*(N+1) for _ in range(K+1)]

# 첫번째 행, 열 초기화
for i in range(1,N+1): # (1,1) ~ (200,200)
    dp[1][i] = 1
for i in range(1,K+1):
    dp[i][1] = i

for i in range(2,K+1): # (2,2) 부터 덧셈
    for j in range(2,N+1):
        dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000000
        
print(dp[K][N])