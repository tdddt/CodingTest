# 이진탐색 O(logN)
# - 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있음
# - 탐색 범위를 절반씩 좁혀가며 데이터 탐색

# 재귀함수로 구현
def recursion(arr,target,start,end):
    if start > end : 
        return None
    
    # 중간점
    mid = (start+end)//2
    
    if(arr[mid] == target):
        return mid
    elif(arr[mid]>target):
        return recursion(arr,target,start,mid-1)
    else:
        return recursion(arr,target,mid+1,end)
    
#recursion(arr,target,0,n-1)
    
# 반복문으로 구현
def repeat(arr,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return None

# 이진탐색트리 : 이진 탐색이 등장할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조
# 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드

# 빠른 입출력
import sys
input = sys.stdin.readline().rstrip()
            
## 복습
def binary(arr,target,start,end):
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return None