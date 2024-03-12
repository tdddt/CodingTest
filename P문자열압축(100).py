# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 채점 결과 : 100/100

def solution(s):
    answer = len(s)
    for i in range(1,len(s)+1):
        temp = []
        temp_s = s
        
        # 문자열 단위로 나누기
        # 나누어 떨어질 때 문자열 분리 개수: (전체 길이 // i), 나누어 떨어지지 않을 때 +1 
        # -> 어차피 전체 길이에 영향을 미치지 않으므로 +1로 설정
        for j in range(len(s)//i+1):
            temp.append(temp_s[:i])
            temp_s = temp_s[i:]
            
        # 압축 문자열 길이 계산
        num_loop = 0
        temp_answer = ""
        start_k=0
        for k in range(len(temp)):
            if(k == len(temp)-1): # 마지막 K 계산
               if(num_loop!=0):
                  howmany = (k-start_k+1) 
                  temp_answer += str(howmany)+temp[k]
                  break
               else : 
                  temp_answer +=temp[k]
                  break
            if(temp[k]==temp[k+1]): # 반복 가능
                if(num_loop==0):
                    start_k=k
                num_loop +=1
            elif(num_loop!=0) or(): # 반복 중지
                howmany = (k-start_k+1) 
                temp_answer += str(howmany)+temp[k]
                num_loop = 0
            else:
                temp_answer+=temp[k]
           
        temp_answer = len(temp_answer)
        if(temp_answer<answer):
            answer = temp_answer
    return answer