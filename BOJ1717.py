# https://www.acmicpc.net/problem/1717

# n+1개의 집합
# 0 a b : 합집합 (a가 포함되어 있는 집합과 b가 포함되어 있는 집합을 합친다는 의미)
# 1 a b : 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산 -> "YES" or "NO" 

n,m = map(int, input().split()) 
mm = [list(map(int,input().split())) for _ in range(m)]
parent = [i for i in range(n+1)] #idx : 원소, 값 : 부모

def find(x): # (4,5) 합치고 (5,6) 합치는 경우 생각하면 재귀 돌려서 찾아야 함 !!
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if(px<py): # 합치기
        parent[py]=px
    else:
        parent[px]=py

for i in range(m):
    a,b,c = mm[i]
    if a==0: # 합집합
        union(b,c)
    elif a==1: # 확인 연산
        # nn에 있는 집한 vs 없는 집합으로 구분
        if(find(b)==find(c)):
            print("YES")
        else:
            print("NO")
            
            