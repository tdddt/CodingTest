# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 채점 결과 : 72/100
# 실패한 테스트 케이스 : 2,7,17,18,20,21,23,27

def solution(s):
    answer = len(s)
    for i in range(1,len(s)+1):
        temp = []
        temp_s = s
        
        # 문자열 단위로 분리
        # 나누어 떨어질 때 문자열 분리 개수: (전체 길이 // i), 나누어 떨어지지 않을 때 +1 
        # -> 어차피 전체 길이에 영향을 미치지 않으므로 +1로 설정
        for j in range(len(s)//i+1):
            temp.append(temp_s[:i])
            temp_s = temp_s[i:]
    
        # 압축 문자열 길이 계산
        num_loop = 0
        temp_answer = len(s)
        start_k=0
        for k in range(len(temp)):
            if(k == len(temp)-1): # 마지막 K
               if(num_loop!=0):
                  origin = i*(k-start_k+1) # 원래 길이 = 단위*반복
                  smaller = i+1 # 압축 길이 = 단위+1
                  temp_answer -= (origin-smaller) # (원래 길이 - 압축길이)만큼 감소
                  break
               else : 
                  break
            if(temp[k]==temp[k+1]): # 반복 가능
                if(num_loop==0):
                    start_k=k
                num_loop +=1
            elif(num_loop!=0) or(): # 반복 중지
                origin = i * (k-start_k+1) # 원래 길이 = 단위*반복
                smaller = i+1 # 압축 길이 = 단위+1
                temp_answer -= (origin-smaller)
                num_loop = 0
                
        if(temp_answer<answer):
            answer = temp_answer
    return answer