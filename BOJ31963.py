# https://www.acmicpc.net/problem/31963

N = int(input())
A = list(map(int, input().split()))

# A를 오름차순으로 만들기
# 어떤 수에 대해 2를 곱하는 연산을 반복 적용하여 A를 오름차순으로 만듦
# 최소 횟수 구하기

ans = 0

# 오름차순인지 확인
for i in range(N-1):
    if(A[i]<A[i+1]): 
        continue
    else:
        while(A[i]>A[i+1]): 
            A[i+1] *=2 
            ans+=1
            
print(ans)