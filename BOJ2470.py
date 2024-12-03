# https://www.acmicpc.net/problem/2470

# 욕액의 특성을 나타내는 정수
# 산성 : 양수, 알칼리성 : 음수
# 혼합용액 특성값 : 각 용액의 합
# 목표 : 2개의 서로 다른 용액을 혼합해서 특성값이 0에 가장 가까운 용액

# 정렬 ㄱ
# 음수와 양수가 섞여 있으면 : 절댓값이 가장 붙어있는 음양으로 ㄱ
# 음수만 있다면 : 가장 큰 값 두 개만 ㄱ
# 양수만 있다면 : 가장 작은 값 두 개만 ㄱ

N = int(input())
arr = list(map(int,input().split(' '))) # 음수 값 있으니까 ' '로 받아야 함
arr = sorted(arr) # 정렬 : arr.sort() 도 가능

# 경우의 수 확인 : if문
if (arr[0]>0 and arr[-1]>0): # 둘 다 양수
    print(arr[0],arr[1])
elif (arr[0]<0 and arr[-1]<0): # 둘 다 음수
    print(arr[-2],arr[-1])
else : # 섞여 있을 때 : 두 합의 절댓값이 가장 작은 경우 찾기
    left = 0 # 음수 아닐 때 까지 이동 가능
    right = N-1 # 양수 아닐 때까지 이동 가능
    ans = abs(arr[left]+arr[right])
    final = [arr[left],arr[right]]
    
    while(left<right):
        x1 = arr[left]
        x2 = arr[right]
        sum = x1+x2
        if(abs(sum)<ans):
            ans = abs(sum)
            final = [x1,x2]
            if ans ==0:
                break
        if sum < 0 : left+=1 # -10 1 
        else : right-=1 # -1 10
    print(final[0],final[1])