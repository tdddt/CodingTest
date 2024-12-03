# https://www.acmicpc.net/problem/1446

# D 킬로미터 길이의 고속도로
# 모든 지름길은 일반통행, 역주행 불가

# 운전해야 하는 거리의 최솟값 구하기

N, D = map(int,input().split()) # N<=12, D<=10000

# 시작 위치, 도착 위치, 지름길 길이
path = [list(map(int,input().split())) for _ in range(N)] 

# 기본 dp는 길이만큼 !
dp = [i for i in range(D+1)]

# for i in range(N):
#     s,e,l = path[i] # start, end, length
#     dp[i] += min(dp[s]+e,l)?
    
# '도착 위치 - 시작 위치 < 지름길의 길이' 라면 필터링
# 이전 도착위치 + 1 = 시작위치 일때부터 지름길 이용 가능 !!
# for i in range(N):
#     s,e,l = path[i] # start, end, length
#     if(e-s<l):
        
for i in range(D + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)  # 이전 지점에서 1km를 이동한 거리로 업데이트
    
    for s, e, l in path: # 만약 스타트 지점인 지름길이 있다면 ...
        if i == s and e <= D:
            dp[e] = min(dp[e], dp[s] + l)
            
print(dp[d])