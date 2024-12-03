# https://www.acmicpc.net/problem/2116

D = int(input())
dice = [[0 for _ in range(6)]for _ in range(D)]
for i in range(D):
    dice[i] = list(map(int,input().split()))

# 서로 같은 숫자 끼리만 쌓을 수 있음! 
# (A,F) (B,D) (C,E) -> (0,5)(1,3)(2,4)
# 긴 옆면 중 어느 한 면의 숫자의 합이 최대가 되도록 주사위 쌓기
# 한 옆면의 숫자 합이 가장 큰 값 출력 -> 위아래 정해지면 옆면은 회전 가능!

for i in range(6): # 처음 어떤 주사위로 시작할건지
    for j in range(6): # 처음 시작한 주사위의 아랫면 정하기
    