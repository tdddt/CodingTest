# https://www.acmicpc.net/problem/2042

# N개의 수 : 빈번한 수의 변경 -> 중간에 구간의 합을 구하려고 함

# N: 수의 개수, M: 수 변경 횟수, K: 구간합 구하는 횟수
N, M, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

'''
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:  # 수 변경
        num[b - 1] = c  # b-1번째 수를 c로 바꾸기
    else:  # 구간 합 계산
        # b-1번째부터 c번째 수까지의 합 출력 (c번째 포함)
        print(sum(num[b - 1:c]))
        
# 1 2 3 4 5 (3번째 수 6으로 변경)
# 1 2 6 4 5 (2번째부터 5번째 수 구간합 계산)
# 17
'''

# 세그먼트 트리로 풀어야 함 !!