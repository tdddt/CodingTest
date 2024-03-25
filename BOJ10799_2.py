# https://www.acmicpc.net/problem/10799

# () : 레이저
# ( : 쇠막대기 시작, ) : 쇠막대기 끝
# 잘린 쇠막대기의 총 개수 = (레이저가 나올 때마다 +열린괄호 개수) + (닫힌괄호마다 +1)
full = input()
full = full.replace("()","*") # 레이저를 *로 교체

ans = 0
open = 0 # 열린 괄호 개수
for i in range(len(full)):
    if(full[i]=="*"):
        ans += open
    elif(full[i]=="("):
        open+=1
    elif(full[i]==")"):
        ans +=1
        open-=1
print(ans)