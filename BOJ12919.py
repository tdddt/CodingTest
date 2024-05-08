# https://www.acmicpc.net/problem/12919

# 두 문자열 S와 T
# S를 T로 바꾸는 게임

# 1. 문자열 뒤에 A추가
# 2. 문자열 뒤에 B를 추가하고 문자열 뒤집기

# 생각할 점1 : T->S로 생각
# 생각할 점2 : BA가 있을 때, 1번 2번 둘 다 적용할 수가 있음 !!
S = list(input())
T = list(input())

def dfs(t):
    if(t==S): 
        print(1)
        exit()
    if(len(t)<=len(S)):
        return
    if(t[-1]=="A"):
        dfs(t[:-1])
    if(t[0]=="B"):
        dfs((t[1:])[::-1])
    return 

dfs(T)
print(0)