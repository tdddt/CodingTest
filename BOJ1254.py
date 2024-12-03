# https://www.acmicpc.net/problem/1254

# 0개 이상의 문자를 문자열 뒤에 추가해서 가장 짧은 문자열 만들고 길이 출력
s = input()
l = len(s)
for i in range(l):
    if(s[i:]==s[i:][::-1]): # i부터 끝까지,뒤집은문자열
        print(l+i) # 팰린드롬인 곳을 찾고 앞에 길이 더해주기!
        break