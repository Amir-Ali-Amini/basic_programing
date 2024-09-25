ls=list(map(int,input().split()))
sm=sum(ls)
if sm%2==1:print (False)
else :
    ll=[0]* (int(sm/2+1))
    ll[0]=1
    for i in ls:
        if i>sm/2:
            print (False)
            break
        else:
            for p in range (len(ll)-1,-1,-1):
                if ll[p]==1:
                    if p+i<len(ll):
                        ll[p+i]=1
    if ll[int(sm/2)]==1:print (True)