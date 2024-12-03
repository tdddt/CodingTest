# https://www.acmicpc.net/problem/1654

# N개 이상의 랜선을 만들어야 함
# 현재 가지고 있는 길이가 제각각인 K개의 랜선
# 만들 수 있는 최대 랜선의 길이 구하기

K, N = map(int,input().split()) 
lan = [int(input()) for _ in range(K)]
lan.sort() # 457 539 743 802

# 이분탐색인가? 투포인터?
# 일단 457로 나눠 .. 
# 457 457 457 457 -> 4개 ..
# 