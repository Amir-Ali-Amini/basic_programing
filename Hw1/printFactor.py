a,b,c,d=map(int,input().split())
a+=1
while a<b:
    if (a%c==0)&(a%d==0):
        print (a)
    a+=1 