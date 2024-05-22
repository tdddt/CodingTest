# https://www.acmicpc.net/problem/2957

# 이진 탐색 트리 : 최대 2개의 자식 노드를 가지는 트리
# 노드 수 : X -> 왼쪽 서브트리에는 X보다 작은 수, 오른쪽 서브트리에는 X보다 큰 수
# insert(X,root)를 몇 번 실행하는지 출력하기

N = int(input())
root = int(input()) # 1
parent_child = [[i,0,0] for i in range(1,N+1)] # (1,2,0) # (parent,left,right)
count = 0

print(count) # root 집어넣을 떄는 count=0

depth = [] 
모르겠음