# https://www.acmicpc.net/problem/1517

# N의 수로 이루어진 수열 A
# 버블 소트를 수행할 때, Swap이 몇 번 발생하는지

N = int(input())
A = list(map(int,input().split()))
ans = 0

def merge_sort(start,end):
    global ans
    if start<end:
        mid = (start+end)//2
        merge_sort(start,mid)
        merge_sort(mid+1,end)
        
        tmp = []
        idx1,idx2 = start,mid+1
        
        while(idx1<=mid and idx2<=end):
            if(A[idx1]<=A[idx2]):
                tmp.append(A[idx1])
                idx1+=1
            else:
                tmp.append(A[idx2])
                idx2+=1
                ans += (mid-idx1)+1
        
        if idx1<=mid:
            tmp = tmp+A[idx1:mid+1]
        if idx2<=end:
            tmp = tmp+A[idx2:end+1]
        
        # 바꾼 순서 저장
        for i in range(len(tmp)):
            A[start+i] = tmp[i]
        
merge_sort(0,N-1)
print(ans)