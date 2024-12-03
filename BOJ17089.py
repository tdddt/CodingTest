# https://www.acmicpc.net/problem/17089
N, M = map(int,input().split()) # N : 사람 수, M : 친구 수 
friend = [[False for _ in range(N)] for _ in range(N)] # friend[A][B]=True 면 친구

# 서로가 모두 친구인 세 사람을 골라서 각각의 친구수를 더한 값의 최솟값 출력
# 세 사람을 고를 수 없는 경우 -1 출력
how = [0 for _ in range(N)] # 친구 몇 명인지

for i in range(M):
    a,b = map(int,input().split())
    friend[a-1][b-1] = True
    friend[b-1][a-1] = True
    how[a-1] +=1
    how[b-1] +=1
    
ans = 12001 # 최대 4000+4000+4000

# 세 사람 => 3중 for 문?
for i in range(N):
    for j in range(i+1,N):
        if not friend[i][j]: # 친구아님
            continue
        for k in range(j+1,N):
            if not friend[i][k] or not friend[j][k]: # 친구아님 / (i,j)는 확실히 친구임
                continue
            ans = min(ans,how[i]+how[j]+how[k]-6) # 서로의 친구 수 빼주기
            
if(ans==12001): print(-1) 
else : print(ans) 