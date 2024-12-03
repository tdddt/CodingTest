# 위에서 아래로

# 하나의 수열에는 다양한 수가 존재
# 크기에 상관없이 나열되어 있음
# 내림차순으로 정렬하는 프로그램

N = int(input())
arr = [ int(input()) for _ in range(N)]

# 삽입 정렬 .. 
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if(arr[j]<arr[j-1]): # 왼쪽 값이 크다면 앞으로 이동
            arr[j],arr[j-1] = arr[j-1],arr[j]
        else : # 왼쪽 값이 크지 않다면 swap
            break   
print(*arr[::-1])
        
        