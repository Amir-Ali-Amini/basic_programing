a,b,c=input().split()
a,b=int(a), int(b)
while a>0:
    d=0
    while d<b:
        print(c,end="")
        if (d==b-1):
            print ('')
        d+=1
    b-=1
    a-=1
