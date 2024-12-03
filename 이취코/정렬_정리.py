# 정렬 -> 이진탐색 가능

arr = [5,3,2,4,1]
# 선택 정렬 O(N^2)
# : 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸기
for i in range(len(arr)):
    idx = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(arr)):
        if(arr[idx] > arr[j]):
            idx =j
    arr[i],arr[idx] = arr[idx], arr[i] # swap

# 삽입 정렬 O(N^2)
# : 한 칸씩 왼쪽으로 이동하다가 자신보다 작은 수를 만났을 때 그 위치에 멈추기
for i in range(1,len(arr)):
    for j in range(i,0,-1): # 인덱스 i부터 인덱스 1까지 감소
        if(arr[j] < arr[j-1]): # 현재 값이 왼쪽 값보다 작다면
            arr[j],arr[j-1] = arr[j-1],arr[j] # swap
        else: # 왼쪽 값보다 작지 않다면
            break
# 버블 정렬
# : 두 개 값 swap 해서 비교 반복
# : 맨 마지막 idx는 정렬됨

# 퀵 정렬 O(NlogN)
# : 피벗 사용. 왼쪽에서 출발해 피벗보다 큰 데이터와 오른쪽에서 출발해 피벗보다 작은 데이터 swap
# : 두 출발이 겹치면 작은 값을 피펏의 위치와 바꿈
# : 분할 상태에서도 동일하게 반복 진행하다가 리스트의 값이 1개면 종료
def quick(arr,start,end):
    if (start>=end): # 원소가 1개라면
        return # 종료
    pivot = start # 피벗은 첫번째 원소
    left = start+1
    right = end
    
    while left<=right:
        # 피벗보다 큰 데이터를 찾을 때까지 left 이동
        while(left<=end and arr[left]<=arr[pivot]):
            left+=1
        # 피벗보다 작은 데이터를 찾을 때까지 right 이동
        while(right>start and arr[right]>=arr[pivot]):
            right+=1
        # 엇갈렸다면 작은 데이터와 피벗 교체
        if left>right:
            arr[right],arr[pivot] = arr[pivot],arr[right]
        # 엇갈리지 않닸다면 작은 데이터와 큰 데이터 교체
        else:
            arr[left],arr[right] = arr[right],arr[left]
            
    # 분할 이후 정렬 재수행
    quick(arr,start,right-1)
    quick(arr,right+1,end)
    
quick(arr,0,len(arr)-1)

# 병합 정렬

# 계수 정렬 O(N+K), N은 데이터의 개수, K는 최대값
# : 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
# : 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 리스트 생성
# -> 리스트의 모든 데이터가 0이 되도록 초기화
# -> 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가
# -> 리스트에는 각 데이터가 몇 번 등장했는지 횟수가 기록되며, 리스트에 저장된 데이터 자체가 정렬된 형태 그 자체.
count = [0]*(max(arr)+1)
for i in range(len(arr)):
    count[arr[i]] +=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')

# 힙 정렬

# sort vs sorted
res = sorted(arr) # sorted(arr, key = arr[1], reverse=True)
arr.sort()

## 복습
# 1. 선택정렬 : 맨 앞 자리와 가장 작은 숫자의 자릿수 swap

# 2. 삽입정렬 : 한 칸씩 왼쪽으로 이동하다가 작은 수 만나면 멈추기

# 3. 퀵정렬 : 피벗 사용. 왼쪽에서 출발해 피벗보다 큰 데이터와 오른쪽에서 출발해 피벗보다 작은 데이터 swap
# 두 출발이 겹치면 작은 값을 피펏의 위치와 바꿈
# 분할 상태에서도 동일하게 반복 진행하다가 리스트의 값이 1개면 종료

# 4. 계수정렬
