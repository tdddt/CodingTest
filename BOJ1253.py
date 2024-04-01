# https://www.acmicpc.net/problem/1253

# 좋다(GOOD) : N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있을 때
# 좋은 수의 개수 출력
# 수의 위치가 다르면 값이 같아도 다른 수

N = int(input())
number = list(map(int,input().split()))

number.sort()

ans=0

# 투 포인터 이용 : 자기자신을 제외한 리스트 생성
for i in range(N):
    temp = number[:i]+number[i+1:]
    
    leftP = 0
    rightP = N-2 # i빼고 인덱스값이므로 -1
    
    while(leftP<rightP):
        tempSum = temp[leftP]+temp[rightP]
        if(tempSum>number[i]):
            rightP-=1
        elif(tempSum<number[i]):
            leftP+=1
        elif(tempSum==number[i]):
            ans+=1
            break
print(ans)
    
'''
N = int(input())
number = list(map(int,input().split()))
ans = 0

can = [] # 가능한 모든 조합의 리스트
for i in range(N):
    for j in range(i+1,N):
       can.append(number[i]+number[j])
       
for i in range(N):
    if(number[i] in can):
        ans+=1
print(ans)
'''