# https://www.acmicpc.net/problem/1213

palindrome = [] # 앞에서 읽어도, 뒤에서 읽어도 똑같이 읽게 되는 문자열
name = list(input().strip())
even_num = []

name.sort(reverse=False) # 오름차순 정렬

for i in range(len(name)):
    if((name[i] in palindrome) or (name[i] in even_num)): # 이미 계산한 문자라면 패스
        continue
    check = name.count(name[i]) # 몇 개 들어있는지
    if(check%2==1): # 홀수라면
        even_num.append(name[i]) # 일단 하나 추가하고
        if(check>2): # 짝수로 가정될 수 있으면 palindrome에 추가
            palindrome.extend([name[i] for k in range(check//2)]) 
    else: # 짝수라면
        # name[i]의 절반만큼 추가
        palindrome.extend([name[i] for k in range(check//2)]) 

if(len(name)%2==1): # 전체 입력 개수가 홀수라면
    if(len(even_num)!=1): # 홀수인 수가 한 개가 아니라면
        print("I'm Sorry Hansoo")
    else: # 출력 : palindrome + even_num + reverse(palindrom)
        result=''.join(map(str,palindrome))+even_num[0]
        palindrome.reverse()
        result+=''.join(map(str,palindrome))
        print(result)
        
else : # 전체 입력 개수가 짝수라면
    if(len(even_num)!=0): # 근데 홀수인 수가 있다면
        print("I'm Sorry Hansoo")
    else: # 출력 : palindrome+reverse(palindrome)
        result=''.join(map(str,palindrome))
        palindrome.reverse()
        result+=''.join(map(str,palindrome))
        print(result)