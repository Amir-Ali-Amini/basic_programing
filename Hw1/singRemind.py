a,b =map(int,input().split())
if a>0: da=1 
else :
    da=0
    a = -1*a
if b>0 : db=1 
else : 
    db=0
    b = -1*b
while a>=b: 
    a-=b 
if a==0:
    print (0)
else:
    if (db==1)&(da==1):
        print (a)
    elif (da==1)&(db==0):
        print (a-b)
    elif (da==0)&(db==0):
        print (-a)
    else :
        print (b-a)