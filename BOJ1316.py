# https://www.acmicpc.net/problem/1316
# 그룹단어 : 나오는 모든 알파벳이 연속으로 나와야 함

n = int(input())
s = [input() for _ in range(n)]

ans = 0
# 그룹 단어의 개수 찾기
for i in s:
    check = True
    new = []
    for j in range(len(i)):
        if i[j] not in new: # 새로 나온 알파벳라면 new에 넣기
            new.append(i[j])
        else: # 이전에 나온 적 있는 알파벳이라면
            if(i[j]!=i[j-1]): # 바로 직전 알파벳랑 다르다면
                check=False
                break
    if(check):
        ans+=1
print(ans)