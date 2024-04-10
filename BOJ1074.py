# https://www.acmicpc.net/problem/1074

N,r,c = map(int,input().split())
sol=0 

# index
# 0 1
# 2 3

def div(N,r,c):
    global sol
    
    if(N==0):
        return
        
    size = int(2**(N-1))
    gap = (size*size) # sol += index*gap
    
    # index 0 : 첫번째 사분면 (1,1)->(1,1)
    if(r<size and c<size):
        div(N-1,r,c)
    # index 1 : 두번째 사분면 (0,2)->(0,0)
    if(r<size and c>=size):
        sol+=1*gap
        div(N-1,r,c-size)
    # index 2 : 세번째 사분면 (3,1)->(1,1)
    if(r>=size and c<size):
        sol+=2*gap
        div(N-1,r-size,c)
    # index 3 : 네번째 사분면 (2,2)->(0,0)
    if(r>=size and c>=size):
        sol+=3*gap
        div(N-1,r-size,c-size)
    
div(N,r,c)
print(sol)