n=int(input())
r=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
sefid=[]
ss=0
for i in range(n):
    ss+=r[i]
    sefid.append(ss)
siah=[]
sb=0
for i in range(m):
    sb+=b[i]
    siah.append(sb)
rrr=max(sefid)
bbb=max(siah)
print(max(0,rrr+bbb,rrr,bbb))
