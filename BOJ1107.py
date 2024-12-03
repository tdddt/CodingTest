# https://www.acmicpc.net/problem/1107

# 리모컨 버튼 0-9 / + / -
# + : +1 
# - : -1
# 0에서 -를 누른 경우 채널이 변하지 않음
# 채널의 개수는 무한대

# 이동하려고 하는 채널 N
# 고장난 버튼이 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야 하는지

now = 100 # 현재 보고 있는 채널
N = int(input()) # 이동하려는 채널
M = int(input()) # 고장난 버튼의 개수
error = list(map(int,input().split())) # 고장난 버튼 리스트

# 1. 일단 최대값 : 100에서 +- 버튼으로만 이동
count = abs(100-N)

# 2. 채널 번호 입력 후 +-로 이동
# N의 최대값 : 500,000 => 0에서 시작할 경우, 1,000,000에서 시작할 경우 고려 => 1,000,001로 범위 제한
for num in range(1000001):
    num = str(num)
    
    # elif 안 쓰고, for - else 로도 작성 가능 : for문이 끝까지 실행된 경우 else가 실행되는 구문
    for i in range(len(num)): # 자릿수
        if int(num[i]) in error: # 고장난 버튼으로 입력해야 하는 숫자면
            break # 입력 불가
        elif i == len(num)-1: # 마지막 자릿수까지 버튼으로 입력 가능하다면
            # 이전 최솟값 vs (+-이동버튼횟수 + 숫자길이) 비교
            count = min(count,abs(int(num)-N)+len(num))
print(count)