# https://www.acmicpc.net/problem/1053

# 4가지 연산
# 1. 문자 삽입 : list.insert(위치,문자)
# 2. 문자 삭제 : list.pop(index)
# 3. 문자 교환(Change) : list[index]
# 4. 서로 다른 문자 교환 : temp 써서 교환

# 1,2,3은 마음껏, 4는 한 번만 사용 가능
# 팰린드롬으로 만들기 위해 필요한 연산의 최솟값 출력

# check4 = False # 4번 사용 여부 : 최대 길이가 50이므로 서로 다른 2개를 뽑아봤자 이중 for문

# dp[i][j] # 1~i-1, j+1~string이 펠린드롬을 만족시킬 때 연산의 최솟값
# i번째와 j번째가 같다면 -> i+1,j-1 탐색
# 아니라면 경우의 수 총 3가지(비용 1추가)
# (1) i번째&(j-1번째) : i번째에 맞추어 j번째 원소를 삭제하거나 / j번째에 맞추어 i번째 원소를 삽입하거나
# (2) (i+1번째)&j번째 : 위와 반대로 적용
# (3) (i+1)&(j-1) : 원소 교환 경우의 수

# dp의 index 지정을 위해 생각해보면
# 1번(삽입)과 2번(삭제)는 같은 연산 -> abaa : (1) 왼쪽 a삽입 (2) 오른쪽 a삭제 -> 둘 다 팰린드롬
# 왼쪽 삽입(=오른쪽 삭제) : dp[l][r-1] -> 교환 비용 1
# 오른쪽 삽입(=왼쪽 삭제) : dp[l+1][r] -> 교환 비용 1
# 교환 : dp[l+1][r-1] (두 수가 같으면 교환비용 발생x)

from collections import deque
MAX = float('inf')

# 경우의 수 3가지
di = [0,1,1]
dj = [-1,0,-1]

quiz = input() # 영어 소문자, 최대 길이 50

def cal_dp(goal):
    result = MAX
    dp = [[MAX]*len(quiz) for _ in range(len(quiz))]
    