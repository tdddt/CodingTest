# https://www.acmicpc.net/problem/1193

target = int(input())

lines = 1
count = 1
while(count<target): # 10 < 14
    lines+=1
    count+=lines # 1+2+3
num = count-target # 10-8 = 2
if(lines%2==0): # 짝수: 끝 lines/1으로 시작 -> i-1,j+1
    print(str(lines-num)+"/"+str(1+num))
else: # 홀수: 끝 1/lines -> i+1,j-1
    print(str(1+num)+"/"+str(lines-num))

# 시간초과 1
# count = 1
# i=1
# j=1
# down = False
# now = 2 # i+j
# while(target!=count):
#     count+=1
#     if(not down):
#         if(i-1>0 and i+j==now):
#             i-=1
#             j+=1
#         else:
#             down = True
#             now+=1
#             j+=1
#     else:
#         if(j-1>0 and i+j==now):
#             i+=1
#             j-=1
#         else:
#             down = False
#             now+=1
#             i+=1
# print(str(i)+"/"+str(j))