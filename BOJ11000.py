# https://www.acmicpc.net/problem/11000

N = int(input()) # 수업 개수
classes = [list(map(int,input().split())) for _ in range(N)]

classes.sort() # 시작 시간 순으로 수업 정렬

end_class = [] # 끝나는 시간 담아두는 용

'''시간 초과나는 코드 : 리스트로 접근함
for start,end in classes:
    if(start in end_class):
        end_class.remove(start) # 이미 들어가 있는 시간을 꺼내주고
        end_class.append(end) # 새로운 종료 시간을 넣어 줌
    else:
        end_class.append(end) # 수업 종료 시간 이력

print(len(end_class))
'''

# 풀이는 맞으나, 시간 초과 -> 우선순위큐를 활용하는 문제 !
# 빨리 시작하는 수업이 항상 빨리 끝난다는 보장은? 
# queue : FIFO (First In, First Out)
# 우선순위 큐(priority queue) : 우선순위가 높은 순위(가장 작은)의 데이터가 먼저 나가는 형태의 자료구조 -> 최소값 : heap[0]
# heapq : 파이썬 내장 모듈로 별도의 설치 작업 필요 없이 바로 사용 가능한 priority queue 알고리즘
# heapq.heappush(heap,item) / heapq.heappop(heap) / heapq.heapify(x) : 리스트 x를 힙으로 변환
'''
# 최대 힙 만들기
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))
'''

import heapq as hq
hq.heappush(end_class,classes[0][1]) # 첫 수업의 끝나는 시간
for i in range(1,N): 
    if end_class[0] <= classes[i][0]: # 끝나는 시간이 시작 수업과 같거나 작을 때
        hq.heappop(end_class) # 해당 수업을 꺼내고 다시 집어넣음
    hq.heappush(end_class,classes[i][1])

print(len(end_class))

