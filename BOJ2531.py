# https://www.acmicpc.net/problem/2531

# 같은 종류의 초밥이 둘 이상 있을 수 있음
# 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
# 초밥의 종류 하나가 쓰인 쿠폰을 발행: 1번 행사에 참가할 경우 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공한다. 
# 만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어서 줌

# 먹을 수 있는 초밥의 가짓수의 최댓값 출력

# 접시 수, 초밥 가짓수, 연속 접시 수, 쿠폰 번호
N, d, k, c = list(map(int,input().split()))
susi = [int(input()) for _ in range(N)] 

ans = 0

# 최댓값 탐색    
for i in range(N):
    tmp = {} # 중복없이 처리해야 하므로 set 이용
    if i <= (N-k):
        tmp = set(susi[i:i+k])
    else :
        tmp = set(susi[i:])
        # add는 하나의 원소를 추가할 때 쓰이고, update는 한꺼번에 여러 개의 원소를 추가할 때 
        tmp.update(susi[:(i+k)%N])
    # 쿠폰 번호가 들어있는지 여부 : 없으면 +1
    if c not in tmp:
        ans = max(ans,len(tmp)+1)
    else:
        ans = max(ans,len(tmp))
print(ans)