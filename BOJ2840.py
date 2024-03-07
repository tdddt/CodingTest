# https://www.acmicpc.net/problem/2840

# N : 바퀴의 칸의 수, K : 바퀴를 돌리는 횟수
N, K = map(int, input().split())

wheel = [ "?" for i in range(N)] 
arrow = 0 # 화살표가 가리키는 칸. 인덱스로 이용.
stop_or_not = False # "!" 출력 여부
used_alphabet=[] # 입력된 글자들의 리스트

for i in range(K):
    # S : 화살표가 가리키는 글자가 몇 번 바뀌었는지
    # stop_str : 회전을 멈추었을 떄 가리키던 글자
    S, stop_str = input().split()
    
    arrow += int(S)
    if(arrow>=N):
        arrow = arrow % N # arrow -= N을 한다면, N을 넘는 숫자가 들어왔을 때 OutOfIndex
    
    if(wheel[arrow]=="?"): # 아직 비어있는 칸이라면
        # 주어진 글자가 이미 기록된 글자인지 확인
        if(stop_str in used_alphabet):
            # 기록된 글자라면 다른 칸에 있는 값과 중복된 글자를 가진다는 뜻
            stop_or_not = True
            break
        else : # 아니라면 바퀴에 기록
            wheel[arrow] = stop_str
            used_alphabet.append(stop_str)
        
    else: # 이미 글자가 들어있는 칸이라면
        # 칸에 있는 글자와 주어진 글자가 다른지 확인
        if(wheel[arrow]!=stop_str):
            stop_or_not = True
            break
        else : # 같다면 그냥 넘기기
            continue
    
# 파이썬 가로로 출력법 
# 1) print list[i], # 끝에 , 붙이기. 단, 요소가 빈칸으로 구분되어 출력됨.
# 2) print(list[i],end='') # end로 출력 제어

if(stop_or_not): # True
    print("!")
else : 
    # 마지막 회전에서 화살표가 가리키는 문자부터, 시계방향으로 출력 (입력을 시계반향으로 했으니 반대방향으로 출력해야함)
    for i in range(N):
        print(wheel[arrow],end="")
        arrow = (arrow-1) % N # 반대방향으로 출력