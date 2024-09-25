
n=input()
n=int(n)
a=[1,1,2,4]
t=3
if n>4:
    while n>4:
        t+=1
        a[t%4]=a[(t-1)%4]+a[(t-2)%4]+a[(t-3)%4]
        n-=1
    print (a[t%4])
elif n==0:
    print(0)
else:
    print (a[n-1])