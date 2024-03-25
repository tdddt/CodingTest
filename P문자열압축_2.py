# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s) # 문자 압축 전
    
    for i in range(1,answer+1): # i : 자르는 문자 단위
        # 문자열 자르기
        newstr = s
        temp = [] # 자른 문자열
        for j in range(len(s)//i+1):
            temp.append(newstr[:i])
            newstr = newstr[i:]
        
        # 문자열 압축 (이전값, 현재값 비교)
        check = temp[0] # 이전값
        count = 1
        szip = ""
        
        for j in range(1,len(temp)+1):
            now = temp[j]
            if(check==now): # 같으면
                count+=1
            else: # 다르면
                if(count==1): # 이전 값 저장
                    szip+= check
                else :
                    szip += (str(count)+check) 
                check = now
                count = 1
    
        # 마지막 값 처리
        if(count==1): # 이전 값 저장
            szip+= check
        else :
            szip += (str(count)+check) 
        # szip = szip.replace("1","") # 1 제거 -> 11이나, 10인 경우 문제 발생
        
        # 압축 후 최소값 비교
        if(answer>len(szip)):
            answer = len(szip)
        
    return answer