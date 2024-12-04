# https://www.acmicpc.net/problem/2563
paper = [[0]*101 for _ in range(101)]
num = int(input())

# 각 크기가 10인 정사각형 모양의 색종이
for _ in range(num):
    a,b = map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            if(i>0 and i<=100 and j>0 and j<=100):
                paper[i][j]+=1
                
ans = 100*num
for i in range(1,101):
    for j in range(1,101):
        if paper[i][j]>1:
            ans -= paper[i][j]-1
            
print(ans)