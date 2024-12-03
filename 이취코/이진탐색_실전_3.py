# 떡볶이 떡 만들기

# 떡의 길이 일정x
# 한 봉지 안에 들어가는 떡의 총 길이는 동일
# 높이 h : h보다 긴 떡은 윗 부분이 잘릴 것이고, 낮은 떡은 잘리지 않음
# 손님이 요청한 길이 M, 잘린 떡만큼 손님이 가져감 -> M만큼의 떡을 위해 절단기에 설정할 수 있는 높이의 최댓값은?

N,M = map(int,input().split()) # 떡의 개수 N, 손님이 요청한 길이 M
rice_cake = list(map(int,input().split()))
rice_cake.sort()

# h는 max(rice_cake)부터 시작
# 하나씩 줄어들면서 가져갈 수 있는 길이 구하기
# 그 길이가 M과 같거나 크다면 정답 출력

ans = 0 # 손님이 가져갈 수 있는 떡의 길이

def cal(h): # h로 잘린 떡의 길이
    return sum([i-h if i-h>=0 else 0 for i in rice_cake])

# 10 15 17 19 -> h를 하나씩 줄이는 것보다 이진탐색으로 ㄱㄱ 
def cut(M,start,end):
    global rice_cake,ans
    while(start<=end):
        mid = (start+end)//2
        tmp = cal(mid) # 잘린 떡의 길이
        if(tmp<M): # 부족한 경우, 더 자르기
            end = mid-1
        else: # 넘는 경우, 덜 자르기
            ans = mid
            start = mid+1
    
cut(M,0,max(rice_cake))
print(ans)