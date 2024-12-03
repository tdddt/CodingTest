# 미래 도시

# 현재 1번 회사 위치. X번 회사에 방문해 물건 판매
# 소개팅 상대는 K번 회사에 존재
# 1번 - K번 - X번 방문 => 플로이드 워셜 알고리즘
# K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간 출력 : 1-K로 가는 최단거리 + K-X로 가는 최단거리 구하기
# X번 회사에 도달할 수 없다면 -1 출력

INF = int(1e9)
N,M = map(int,input().split()) # N: 회사 개수, M: 경로 개수
start = 1 # 1번 회사에서 출발
# graph = []*(N+1) # 간선 정보
# visited = [False]*(N+1) # 방문 여부
graph = [[INF]*(N+1) for _ in range(N+1)]

# 초기화
for a in range(1,N+1):
    for b in range(1,N+1):
        if a==b : graph[a][b]=0
        
# 간선 정보
for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
X,K = map(int,input().split())

# 그래프 채우기
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 1-K로 가는 최단거리 + K-X로 가는 최단거리
ans = graph[1][K]+graph[K][X]

if ans>=INF: print("-1")
else: print(ans)
