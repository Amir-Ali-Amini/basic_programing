def max(x,y):
    if x>y:
        x,y=y,x
    if y%x==0:
        return x
    else :
        return max (x , y%x)
a,b=map(int,input().split())
print (int(a*b/max(a,b)))