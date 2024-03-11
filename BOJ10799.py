# https://www.acmicpc.net/problem/10799

# 쇠막대기 : 왼쪽 끝은 여는 괄호, 오른쪽 끝은 닫는 괄호
# 레이저 : () -> 다른 문자로 대체하기

laser=input()
laser=laser.replace("()","?")
laser=list(laser)

open_num = 0
ans = 0
for i in range(len(laser)):
   if(laser[i]=="?"):
      ans += open_num
   elif(laser[i]=="("):
      open_num+=1
   elif(laser[i]==")"):
      ans+=1
      open_num-=1
print(ans)
