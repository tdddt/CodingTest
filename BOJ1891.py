# https://www.acmicpc.net/problem/1891

# 341 : 3번 사분면의 4번 사분면의 1번 사분면
# 길이가 x면, 총 사분면의 개수는 4^x, 한 변의 크기는 2^x

d,p = input().split() # d:자릿수, p:조각번호
d = int(d)
x,y = list(map(int,input().split())) # x:좌우 이동, y:상하이동

# 도착한 사분면의 번호 출력, 존재하지 않는 사분면인 경우에는 -1 출력
# 분할정복? 사분면을 좌표화?

# p:조각번호, idx:조각번호 인덱스, r:x좌표, c:y좌표, size: 한 사분면의 크기
def find(idx,r,c,size): # 축소해가며 좌표찾는 함수
    global p
    if size==0:
        return r,c
    if p[idx]=='1':
        return find(idx+1,r,c+size,size//2)
    elif p[idx]=='2':
        return find(idx+1,r,c,size//2)
    elif p[idx]=='3':
        return find(idx+1,r+size,c,size//2)
    elif p[idx]=='4':
        return find(idx+1,r+size,c+size,size//2)

# m,n = 좌표
m,n = find(0,0,0,(2**d)//2) # 좌표 찾기

# 새로운 사분면 조각의 좌표
new_m,new_n = m-y,n+x

def sol(new_m,new_n,size,ans): # 조각번호 찾기
    if size==0:
        print(ans)
        return
    if 0<=new_m<size and size<=new_n<2*size:
        sol(new_m,new_n-size,size//2,ans+'1')
    elif 0<=new_m<size and 0<=new_n<size:
        sol(new_m,new_n,size//2,ans+'2')
    elif size<=new_m<2*size and 0<=new_n<size:
        sol(new_m-size,new_n,size//2,ans+'3')
    elif size<=new_m<2*size and size<=new_n<2*size:
        sol(new_m-size,new_n-size,size//2,ans+'4')
    
if(0<=new_m<2**d and 0<=new_n<2**d):
    sol(new_m,new_n,(2**d)//2,'')
else:
    print(-1)