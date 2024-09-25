a,b=map(int,input().split())
c=a
d=b
if a==0:
    if b>0:
        print (b)
    else :
        print (a)
if a>0:
    while a>0:
        a-=1 
        b-=1 
    if b>0: print ( d)
   # elif b==0 : print ( ' a = b')
    else : print ( c)
if a<0:
    while a<0:
        a+=1 
        b+=1 
    if b>0: print ( d)
  #  elif b==0 : print ( ' a = b')
    else : print ( c)

    