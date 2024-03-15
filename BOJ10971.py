# https://www.acmicpc.net/problem/10971
# W[i][j] : i에서 j로 가기 위한 비용
# 가장 적은 비용을 들이는 순회 여행(도시를 모두 거쳐야 함) 경로
# 한 번 갔던 도시로는 갈 수 없음
# 출발 지점은 정해져 있지 않음

# 시작도시, 현재도시, 방문비용, 방문횟수
def dfs_backtracking(start, now, now_sum, cnt):
    global N, map, min_sum, visited
    if(cnt==N): # 도시를 모두 돌았다면 멈추기
        if map[now][start] : # 길이 0이 아니라면(=길이 있다면)
            now_sum+=map[now][start] # 시작 도시로 되돌아가기
            if now_sum < min_sum: # 최소 비용인지 확인
                min_sum = now_sum
        return # 길이 0이라면 유효한 순회X
    if now_sum>min_sum: # 방문 비용이 커지면 계산할 필요 X
        return
    
    for i in range(N): # 다음으로 넘어갈 도시들
        if(not visited[i] and map[now][i]): # 방문 안 한 곳이고, 길이 0이 아니라면
            visited[i]=1
            dfs_backtracking(start,i,now_sum+map[now][i],cnt+1)
            visited[i]=0
    
N = int(input()) # N : 도시의 수
map = [list(map(int,input().split())) for _ in range(N)]

# dfs backtraking 이용
visited = [0] * N # 방문 여부

import sys
min_sum = sys.maxsize # 최소인 방문 비용

for i in range(N):
    visited[i]=1 # 시작도시
    dfs_backtracking(i,i,0,1) 
    visited[i]=0 # 다음 계산을 위해 풀어주기

print(min_sum)
    
    


    