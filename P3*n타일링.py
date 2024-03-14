# https://school.programmers.co.kr/learn/courses/30/lessons/12902
# 풀이 참고 : https://velog.io/@bjo6300/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-3xn-%ED%83%80%EC%9D%BC%EB%A7%81

def solution(n):
    if n % 2 != 0 : # n은 짝수여야 함
        return 0
    
    dp = [0] * (n+1) # dp 생성
    dp[2] = 3
    # dp[4] = 11
    
    for i in range(4,i+1,2):
        dp[i] = dp[i-2]*3 # 직전N * (n=2일 떄, 경우의 수 3개)
        for j in range(i-4,-1,-2):
            dp[i] += dp[j]*2 # 겹치지 않게 특이한 경우 2개만 곱해줌
        
        dp[i]=dp[i]+2 # 새로운 경우의 수 +2
        dp[i]%=1000000007 # for 나머지 return
    
    return dp[n]