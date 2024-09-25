def expon(x,p):
    c,d=0,1
    for z in range (1,p+1):
        c+=d
        d*=x/z
    print ((c//0.0001)*0.0001)
a,b=map(int,input().split())
expon(a,b)