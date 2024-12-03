# https://www.acmicpc.net/problem/12931

# 모든 값이 0으로 채워져 있는 길이가 N인 배열 A
# 1) 값 하나를 1 증가
# 2) 모든 값을 두 배 증가 -> 최소 1)을 1번해야 가능

# 배열 B가 주어졌을 때, A를 B로 만들기 위한 최소 연산 횟수

N = int(input())
A = [0 for _ in range(N)]
B = list(map(int, input().split()))

# 일단 B가 0이 아닌 수에 대해 A에 1번 실행
# 아래 루프 반복
# B와 같은지 확인
# if(가장 작은 값 >= 2배): 2배 증가

# A->B가 아니라 B->A로 ㄱ?
# 1) 홀수 값 하나를 -1
# 2) 값을 /2
# 마지막에 1인 애들을 0으로 만들기 위해서는 그 개수만큼 1번 적용해야 함

# 일단 전부 2로 나눔 .. 
# 아니다 일단 홀수인 애들 각각에 대해 1번 적용해야 나눌 수 있음(홀수 수만큼 ㄱㄱ)
# 전부 2로 나눔 (1번) 
# 근데 홀수 있으면 또 -1
# 2로 나누기 반복
# 1인 경우 -1 ... 그냥 홀수처리랑 동일
# 홀수처리한 뒤에 중간에 0 이되면 stop..

ans = 0 
while True:
    for i in range(N): # 홀수일 경우
        if(B[i]%2==1):
            B[i]-=1
            ans+=1
    if sum(B)==0 : # 전부 0이 되면
        break
    for i in range(N): # 홀수가 처리됐다면 전부 2로 나누기 가능
        B[i]/=2
    ans+=1
print(ans)