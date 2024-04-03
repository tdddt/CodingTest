# https://www.acmicpc.net/problem/11404

# n개의 도시
# 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스 / 버스 비용
# 도시 A에서 B로 가는데 필요한 비용의 최솟값 구하기

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

mm = [[ float("inf") for _ in range(n)] for _ in range(n)]

for i in range(m):
    temp = list(map(int,input().split())) # 출발도시 도착도시 비용
    mm[temp[0]-1][temp[1]-1] = min(mm[temp[0]-1][temp[1]-1],temp[2])
    
# 플로이드-와샬 알고리즘
for k in range(n): # 경유지 
    for i in range(n): # 출발지
        for j in range(n): # 도착지
            mm[i][j] = min(mm[i][j],mm[i][k]+mm[k][j])

# inf인 경우, 0으로 바꿔주기
for i in range(n):
    for j in range(n):
        if(mm[i][j]==float("inf") or i==j):
            mm[i][j]=0
# 출력
for i in range(n):
   print(*mm[i])