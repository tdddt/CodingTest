# https://www.acmicpc.net/problem/3190

# NxN 정사각 보드, 사과가 놓여있는 칸
# 뱀은 맨위맨좌측, 길이는 1, 오른쪽으로

N = int(input()) # 보드크기 NxN

K = int(input()) # 사과 개수
apple = [list(map(int,input().split())) for _ in range(K)] # 사과의 위치
    
L = int(input()) # 뱀의 방향 변환 정보(정수X, 문자C)
change = [list(map(str,input().split())) for _ in range(L)] # X초 뒤 L(왼쪽) or D(오른쪽)

snake = [1,1] # snake 머리 위치
snakeL = [snake[:]] # snake 길이-1(뱀의 몸통), 뱀이 지나온 곳
dir = "R" # L(왼쪽), R(오른쪽), U(위), D(아래)
sec = 0 # 게임 초 
    
while(True):
    sec+=1
    # 방향전환 여부 확인 및 머리 이동 (X초가 끝난 뒤에 회전 !!!)
    if(len(change)>0 and sec == int(change[0][0])):
        changeD = change[0][1]
        if(dir=="L"):
            snake[1] -=1
            if(changeD=="L"):
                dir = "D"
            else:
                dir = "U"
        elif(dir=="R"):
            snake[1] +=1
            if(changeD=="L"):
                dir="U"
            else:
                dir = "D"
        elif(dir=="U"):
            snake[0]-=1
            if(changeD=="L"):
                dir="L"
            else:
                dir="R"
        elif(dir=="D"):
            snake[0]+=1
            if(changeD=="L"):
                dir="R"
            else:
                dir="L"
        del change[0]
    else:
        if(dir=="L"):
            snake[1] -=1
        elif(dir=="R"):
            snake[1] +=1
        elif(dir=="U"):
            snake[0] -=1
        elif(dir=="D"):
            snake[0] +=1
    
    if(snake[0]>N or snake[1]>N or snake[0]<1 or snake[1]<1) : # 벽 부딪힘 확인
        # print("벽 부딪힘 ㅠㅠ")
        break  
    elif(snake in snakeL): # 꼬리랑 닿음 확인
        # print("꼬리랑 닿음 ㅠㅠ")
        break 
    else:
        snakeL.append(snake[:])
    
    # 사과 확인
    if(snake in apple):
        apple.remove(snake)
    else:
        del snakeL[0]
        

print(sec)