# https://www.acmicpc.net/problem/14225

# 수열 S가 주어졌을 때,
# 수열 S의 부분 수열의 합으로 나올 수 "없는" 가장 작은 자연수를 구하는 프로그램

import heapq

N = int(input())
S = list(map(int,input().split()))
canSum = []

# 가능한 수열의 합을 조합으로 미리 계산하기
from itertools import combinations
for i in range(1,N+1):
    temp = list((combinations(S,i)))
    for j in temp:
        heapq.heappush(canSum,sum(j))

ans = canSum[-1]+1
# canSum = list(set(canSum)) # 중복제거

i=1
last = 0 # 중복 판단
while(len(canSum)>0):
    temp = heapq.heappop(canSum)
    if(last==temp):
        continue
    if i == temp:
        i+=1
        last = temp
        continue
    else:
        ans=i
        break
    
print(ans)