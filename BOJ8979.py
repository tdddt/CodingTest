# https://www.acmicpc.net/problem/8979

# 1. 금메달 수 더 많은 나라
# 2. 금메달 수가 같으면, 은메달 수가 더 많은 나라
# 3. 금,은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

# 각 국가는 정수로 표현
# 등수 : (자신보다 더 잘한 나라 수)+1
# 금,은,동메달 수가 모두 같다면 두 나라의 등수는 같음

N, K = map(int, input().split()) # N : 국가의 수, K : 등수를 알고 싶은 국가

country = [ [0,0,0,0] for _ in range(N+1)]

for i in range(N):
    # country, gold, silver, bronze
    c,g,s,b = map(int, input().split())
    country[i] = [c,g,s,b]
    
country.sort(key=lambda x: (-x[1],-x[2],-x[3])) # 조건에 따라 정렬

rank = 1

samecount = 0
samecheck = False

if(country[0][0]==K):
    print(rank)
    exit()

for i in range(1,N):
    rank+=1
    # 만약 앞에 나온 나라와 gsb가 똑같다면
    if(country[i][1:]==country[i-1][1:]):
        samecount+=1
        samecheck=True
    else:
        samecount=0
        samecheck=False
    if(country[i][0]==K): # 등수를 알고 싶은 국가라면
        break

# samecheck가 True일 때는 rank-samecount, False일 때는 rank 출력
if(samecheck):
    print(rank-samecount)
else:
    print(rank)