n,k =map(int,input().split())
ls=[0]*n*2
list=[]
t=1
q=0
while 1:
    if ls[t]==0:
        ls[t]=1
        list.append(t)
        q+=1
        if list[-1]==n:
            print (len(list))
            break
        if q%k==0:
            d=t-k
            list.append(int(((t*(t+1))/2)-(d*(d+1))/2))
            if int(((t*(t+1))/2)-(d*(d+1))/2)<n:
                ls[int(((t*(t+1))/2)-(d*(d+1))/2)]+=1
    t+=1
    if list[-1]==n:
        print (len(list))
        break