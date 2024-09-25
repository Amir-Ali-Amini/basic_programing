a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())
c1,c2,c3=map(int,input().split())
msrf,hzine=map(int,input().split())
if (msrf>a1)&(msrf<c2):
    if (msrf<a3)or((msrf>b1)&(msrf<b3))or((msrf>c1)&(msrf<c3)):
        print (msrf*hzine)
    else:
        print(msrf * hzine *2)
    