# https://www.acmicpc.net/problem/1213

# 영어 이름을 팰린드롬으로 바꾸는 프로그램
# 불가능할 때는 "I'm Sorry Hansoo" 출력
# 팰린들롬 : 앞에서 읽어도, 뒤에서 읽어도 같은 글자
# 정답이 여러개일 경우에는 사전순으로 앞서는 것을 출력

name = list(input().strip())
name.sort() # 사전순으로 정렬 'A''A''B''B'

ans = "" # 정답의 절반
odd = [] # 정답의 가운데
alphabet = name[0] # 이전 값
count = 1

# 알파벳 개수 세기
for i in range(1,len(name)):
    now = name[i] # 현재 값
    if(now==alphabet): # 이전 알파벳과 같을 떄
        count+=1
    else : # 이전 알파벳과 다를 때
        # 지금까지의 결과 저장
        if(count%2==0): # 짝수번 등장
            ans += (alphabet*(count//2))
        else: # 홀수번 등장
            ans += (alphabet*(count//2))
            odd.append(alphabet)
        # 이번 결과 추가
        alphabet = now
        count = 1

# 마지막 값 결과 추가
if(count%2==0): # 짝수번 등장
    ans += (alphabet*(count//2))
else: # 홀수번 등장
    ans += (alphabet*(count//2))
    odd.append(alphabet)
    
# 출력   
if(len(name)%2==0): # 전체 수가 짝수일 떄
    if(len(odd)>=1): # 홀수가 있다면 불가
        print("I'm Sorry Hansoo")
    else:
        print(ans,end="")
        print(ans[::-1],end="")
    
else: # 전체 수가 홀수일 떄
    if(len(odd)>1): # 홀수가 하나 이상이라면 불가
        print("I'm Sorry Hansoo")
    else:
        print(ans,end="")
        print(odd[0][0],end="")
        print(ans[::-1],end="")