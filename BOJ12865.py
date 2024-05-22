# https://www.acmicpc.net/problem/12865

# N개의 물건(무게W, 가치V), 최대 K만큼의 무게

N,K = list(map(int,input().split())) # 물건개수 N, 최대무게 K
thing = [list(map(int,input().split())) for _ in range(N)] #[w,v] (무게,가치)
# thing.sort() # 오름차순 정렬
# ans = 0

dp = [[0]*(K+1) for _ in range(N+1)]
thing.insert(0,[0,0]) # index 1부터 시작하기 위해서 맨 앞에 [0,0] 삽입
for i in range(1,N+1): # i 번째 물건
    w,v = thing[i] 
    for j in range(1,K+1): # 가방 최대 무게가 j일 때
        if j<w: #물건이 안 들어가는 경우, 이전 표값으로 채움
            dp[i][j] = dp[i-1][j]
        else: #물건이 들어가는 경우, max값 찾기
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)

print(dp[N][K])