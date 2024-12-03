# https://www.acmicpc.net/problem/16931

# input
N,M=map(int,input().split())

# 패딩
paper = [[ 0 for _ in range(M+2)] for _ in range(N+2)]
for i in range(N):
    paper[i+1] = [0]+list(map(int,input().split()))+[0]
    
# 양 끝 모서리 : 1 or N or M 
ans = 0
ans += (N*M) + (N*M) # 바닥, 천장 더해주기
    
# 상하좌우에 작은 수가 있다면 +(차이*1)
# 빈 곳은 0으로 판단
for i in range(1,N+1):
    for j in range(1,M+1):
        now = paper[i][j]
        #상
        if(now>paper[i-1][j]):
            ans += (now-paper[i-1][j])

        #하
        if(now>paper[i+1][j]):
            ans += (now-paper[i+1][j])
        
        #좌
        if(now>paper[i][j-1]):
            ans += (now-paper[i][j-1])
            
        #우
        if(now>paper[i][j+1]):
            ans += (now-paper[i][j+1])
print(ans)