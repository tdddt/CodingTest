# https://www.acmicpc.net/problem/2531

# 시간초과 코드

# 같은 종류의 초밥이 둘 이상 있을 수 있음
# 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공
# 초밥의 종류 하나가 쓰인 쿠폰을 발행: 1번 행사에 참가할 경우 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공한다. 
# 만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어서 줌

# 먹을 수 있는 초밥의 가짓수의 최댓값 출력

# 접시 수, 초밥 가짓수, 연속 접시 수, 쿠폰 번호
N, d, k, c = list(map(int,input().split()))
susi = [int(input()) for _ in range(N)] 

susi_len = len(list(set(susi)))
ans = 0
all_susi = []

# 전체 경우의 수 구하기
for i in range(N): # 0~6
    tmp = []
    for j in range(k): # 
        tmp.append(susi[(i+j)%N])
    all_susi.append(tmp)

# 최댓값 탐색    
for i in range(len(all_susi)):
    tmp = len(list(set(all_susi[i]))) # 중복 제거한 가짓수
    # 쿠폰 번호가 들어있는지 여부 : 없으면 +1
    if c not in all_susi[i]:
        tmp+=1
    ans = max(ans,tmp)
print(ans)