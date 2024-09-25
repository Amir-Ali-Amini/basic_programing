n = int(input())
def zir (n):
    if n==0:
        return [[]]
    else :
        ll=[]
        ls = zir(n-1)
        for i in ls:
            ll.append(i+[n])
        return ls+ll
sub=zir(n)
m=int(input())
mm=list(map(int,input().split()))
if m==2:
    for i in sub[mm[0]]:
        print (i,end=' ')
else :
    for i in range (len(sub) ):
        if sub[i]==mm:
            print (i)
            break