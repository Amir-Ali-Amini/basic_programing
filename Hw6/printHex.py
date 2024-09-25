def bini(x):
    d,t=0,1
    for i in range (-1,-len(x)-1,-1):
        if x[i]=='1':
            d+=t
        t*=2
    return (d)
def hexi(x):
    d=[]
    while x>0:
        d+=[x%16]
        x=x//16
    q=''
    for i in range (-1,-len(d)-1,-1):
        if d[i] <10:
            q+=str(d[i])
        else:
            q+=(chr(87+d[i]))
    return q
n=input()
if int(n)==0:
    print('0')
else:
    print (hexi(bini(n)))