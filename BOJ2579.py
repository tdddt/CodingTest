# https://www.acmicpc.net/problem/2579
# 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임
# 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 됨

# 규칙
# 1) 계단은 한 번에 한 계단씩 or 두 계단씩 가능
# 2) 연속된 3개의 계단을 모두 밟아서는 안 됨.(시작점은 계단 포함x/최대 2개까지 밟을 수 있음)
# 3) 마지막 도착 계단은 반드시 밟아야 함

# 총 점수의 최댓값을 구하는 프로그램

N = int(input()) # 계단의 개수
stairs = [int(input()) for _ in range(N)] # 계단 점수
stairs.insert(0,0) # dp와 i변수 맞추기 위해

# dp[n] : n번째 계단에 올랐을 때 얻는 점수의 최댓값
dp = [0]*(N+1) # n<=300 # 계단의 개수가 2개이하일 경우 오류 발생하므로 그냥 301 ㄱㄱ 하고 for문에서 정지

dp[1] = stairs[1]

if(N>1): # if문 잊지말기
    dp[2] = stairs[1] + stairs[2]

# 1+3 or 2+3 가능 1+2+3은 연속된 3개라서 불가능
if(N>2):
    dp[3] = max(stairs[1]+stairs[3],stairs[2]+stairs[3])

for i in range(4,N+1):
    # 한 칸을 건너뛰고 이번 계단을 밟느냐 or 안 건너뛰고 이번 계단을 밟느냐
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    
    # i-3 / i-2 / i-1 / i => (i-3)+(i-1)+i or (i-2)+i
    # dp[i-1]을 안 보는 이유 : 만약 걔가 이미 2개의 계단을 밟은 상태라면 문제 발생 !
    
print(dp[N])