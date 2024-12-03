# https://www.acmicpc.net/problem/1377

# 시간초과나서 추가한 코드
import sys
input = sys.stdin.readline

N = int(input()) # 배열의 크기
arr = []
for i in range(N):
    arr.append((int(input()),i)) # 튜플 (값, idx)

after = sorted(arr) # 정렬 전후 인덱스 비교
ans=0

for i in range(N):
    ans = max(ans,after[i][1]-arr[i][1])

print(ans+1)

# 한 사이클에 왼쪽으로는 한 칸만 이동 가능! (가장 큰 양수값 +1)
# 10 1 5 2 3 -> 1 2 3 5 10
# 0  1 2 3 4 -> 1 3 4 2 0
# after[i][1] - arr[i][1]
# 1 2 2 -1 -4 : 최댓값+1

## 이전 아이디어
# 버블 소트 : 인접한 2개 비교해서 swap
# 출력 값 : 정렬일 때 i 값 -> 전체 정렬 swap turn을 몇 번 했는지

# 10 1 5 2 3, N=5 => 1 2 3 5 10
# i=1 -> j=1~j=4 : 1 10 5 2 3 -> 1 5 10 2 3 -> 1 5 2 10 3 -> 1 5 2 3 10
# i=2 -> j=1~j=3 : 1 2 5 3 10 -> 1 2 3 5 10
# i=3 -> j=1~j=2 : 완료!

# 몇 개의 값이 안 맞는지?
# 10<1 x
# 1<5 o
# 5<2 x
# 2<3 o
# => 최소 2번은 돌아야 함 + 확인 과정 1

# ans = 1
# for i in range(N-1):
#     if(arr[i]>arr[i+1]):
#         ans+=1
# print(ans)