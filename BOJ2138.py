# https://www.acmicpc.net/problem/2138

# N개의 스위치, N개의 전구 (0,1)
# 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태
# i번째 스위치를 누르면 i-1,i,i+1의 전구 상태가 바뀜
# 불가능한 경우, -1 출력

N = int(input())

now = list(map(int, input()))
wannabe = list(map(int,input()))

def change(number):
   if(number==0):
      return 1
   elif(number==1):
      return 0

# 스위치 전환 함수 
def turn(light,i):
    light[i] = change(light[i])
    if(i>0):
        light[i-1] = change(light[i-1])
    if(i<N-1):
        light[i+1] = change(light[i+1])

sub_now = now[:] 
turn(sub_now,0) # 첫번째 스위치를 눌렀을 경우

ans = 0
sub_ans = 1

# 바로 이전 인덱스가 다르면, 다음 인덱스를 바꿈
# 첫번째 스위치를 누르지 않은 경우
for i in range(1,N):
    if(now[i-1]!=wannabe[i-1]):
        turn(now,i)
        ans+=1
if(now!=wannabe):
    ans = 100001
    
# 첫번째 스위치를 누른 경우
for i in range(1,N):
    if(sub_now[i-1]!=wannabe[i-1]):
        turn(sub_now,i)
        sub_ans+=1
if(sub_now!=wannabe):
    sub_ans= 100001

answer = min(ans, sub_ans)
if answer == 100001 :
  print(-1)
else :
  print(answer)