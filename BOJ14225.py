# https://www.acmicpc.net/problem/14225

# 수열 S가 주어졌을 때,
# 수열 S의 부분 수열의 합으로 나올 수 "없는" 가장 작은 자연수를 구하는 프로그램

N = int(input())
S = list(map(int,input().split()))
canSum = []

# for 문 돌면서 못 만들면 출력하기
# 1. 수열에 있는 경우 2. 수3열의 합으로 만들 수 있는 경우

# 가능한 수열의 합을 조합으로 미리 계산하기
from itertools import combinations
for i in range(1,N+1):
    temp = list((combinations(S,i)))
    for j in range(len(temp)):
        canSum.append(sum(temp[j]))

# canSum.sort()

i = 1
while(True):
    if i in canSum:
        i+=1
    else:
        print(i)
        break

    