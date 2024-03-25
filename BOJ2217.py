# https://www.acmicpc.net/problem/2217

# N개의 로프
# K개의 로프를 사용하여 중량이 w인 문체를 들어올 떄, 각각의 로프에는 w/k만큼의 중량이 걸리게 됨

# 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량
N = int(input())
rope = [ int(input()) for _ in range(N)]

# 가장 강한 로프부터 정렬
rope.sort(reverse=True)

sol = rope[0] # 가장 강한 로프
for i in range(1,N):
    # 전체 로프가 버틸 수 있는 최대 중량 = 추가된 로프의 최대 중량 * 로프 개수
    addRope = rope[i]*(i+1)
    if(addRope>sol):
        sol = addRope
print(sol)