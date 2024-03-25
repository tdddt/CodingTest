# https://www.acmicpc.net/problem/2840

# 바퀴에 같은 글자 두 번 이상 등장 X
# 시계방향으로 돌아감
# K번 바퀴 돌리기 -> 글자 변한 횟수, 어떤 글자에서 멈추었는지

N,K = map(int,input().split()) # 바퀴 칸의 수, 바퀴 돌리는 횟수
wheel = ["?" for _ in range(N)]

S = [list(input().split()) for _ in range(K)]

check = 0
find = True
used = [] # 사용된 글자

for i in range(K):
    check += int(S[i][0])
    check %= N
    if(wheel[check]=="?"): # 빈 칸이라면 채워주기
        if(S[i][1] in used): # 사용된 글자인지 체크
            find=False
            break
        wheel[check]=S[i][1]
        used.append(S[i][1])
    elif(wheel[check]==S[i][1]): # 이미 값이 있는 칸, 들어갈 글자와 같음
        continue
    else: # 이미 값이 있는 칸, 들어갈 글자와 다름
        find = False
        break

# 마지막 회전에서 화살표가 가리키는 문자부터 시계방향으로 바퀴에 적어놓은 알파벳 춫력
# 결정하지 못한 칸은 '?' / 해당하는 바퀴가 없다면 "!" 출력
if (find):
    for _ in range(N):
        check%=N
        print(wheel[check],end="")
        check-=1
else:
    print("!")
