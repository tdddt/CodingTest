# https://www.acmicpc.net/problem/2941
given = input()
al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
ans = 0
for i in al:
    while(i in given):
        s = given.find(i) #0
        idx = len(i) #2
        given = given[:s]+" "+given[s+idx:]
        ans+=1
ans+=len(given.replace(" ",""))
print(ans)