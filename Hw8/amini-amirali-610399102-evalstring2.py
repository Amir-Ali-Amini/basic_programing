def spl(x):
    a=['+','-','*','=','/']
    ls=[]
    j=0
    i=1
    while i <len(x):
        if x[i]in a:
            ls.append(int (x[j:i]))
            ls.append(x[i])
            j=i+1
            if i<len(x)-1:
                if x[i+1]=='-':i+=1
        i+=1
    return ls
n=input ()
n=spl(n)
i=1
while i< len (n)-2:
    if n[i]=='*':
        n[i-1]=n[i-1]*n[i+1]
        del (n[i:i+2])
        i-=1
    if n[i]=='/':
        n[i-1]=n[i-1]/n[i+1]
        del (n[i:i+2])
        i-=1
    i+=1
i=0
while i< len (n):
    if n[i]=='+':
        n[i-1]=n[i-1]+n[i+1]
        del (n[i:i+2])
        i-=1
    if n[i]=='-':
        n[i-1]=n[i-1]-n[i+1]
        del (n[i:i+2])
        i-=1
    i+=1
i=0
print (int(n[0]))