# 거스름돈

# 500원, 100원, 50원, 10원짜리 동전 
# 손님에게 거슬러 줘야 할 돈 : N원 (10의 배수)
# 동전의 최소 개수는? 

N = int(input())
ans = 0
# 일단 500원으로 나눈 뒤,
# ans+=N//500, N=N%500
if(N>=500):
    ans+=N//500
    N%=500
if(N>=100):
    ans+=N//100
    N%=100
if(N>=50):
    ans+=N//50
    N%=50
if(N>=10):
    ans+=N//10
    N%=10
print(ans)

# 정답 코드
# coins = [500,100,50,10]
# for coin in coins:
#     ans+=N//coin
#     N%=coin
# print(ans)