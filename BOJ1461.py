# https://www.acmicpc.net/problem/1461

# 현재 위치 = 사람들이 마구 놓은 책 위치 = 0
# 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램
# 한 번에 최대 M권의 책을 들 수 있음

N,M = map(int,input().split()) # 전체 책의 개수, 한 번에 들 수 있는 책의 개수
loc = list(map(int,input().split(' ')))

# 가장 멀리 갔다가 놓으면서 돌아오기..? 
# ㄴㄴ 근데 다 놓으면 돌아올 필요 없으니까 맨 마지막에 가장 먼 책 놓고 오기
negative = []
positive = []

# 가장 마지막 책
loc.sort()
# last = loc[-1] : 이렇게 하면 틀림 !! -> 음수, 양수 중 가장 먼 거리를 찾아야 함 !!!!
last = max(abs(loc[0]),abs(loc[-1]))

for i in range(N):
    if(loc[i]<0):
        negative.append(abs(loc[i])) # 절댓값으로 넣어줘야 계산이 편함
    else:
        positive.append(loc[i])

# 내림차순 정렬
negative.sort(reverse=True)
positive.sort(reverse=True)

ans=0

for i in range(0,len(negative),M):
    ans += negative[i]*2 # 되돌아오는 걸음까지 포함
for i in range(0,len(positive),M):
    ans += positive[i]*2
    
print(ans-last)