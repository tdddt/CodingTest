# 부품 찾기

# N개의 부품
# 각 부품은 정수 형태의 고유한 번호
# 손님이 M개 종류의 부품을 대량으로 구매
# 가게 안에 부품이 모두 있는지 확인하는 프로그램

import sys
input = sys.stdin.readline

N = int(input().rstrip())
thing = list(map(int,input().rstrip().split()))
thing.sort()
M = int(input().rstrip())
order = list(map(int,input().rstrip().split()))
ans = ["no"] * M

def check_order(target,start,end):
    global thing
    while start<=end:
        mid = (start+end)//2
        if(thing[mid]==target):
            return True
        elif(thing[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return False

for i in range(M):
    # if order[i] in thing:
    if(check_order(order[i],0,N-1)): # 값이 있다면
        ans[i]="yes"
        
print(*ans)