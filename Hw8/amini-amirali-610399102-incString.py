def plus(n,x):
    if n[x]=='0':n[x]='1'
    elif n[x]=='1':n[x]='2'
    elif n[x]=='2':n[x]='3'
    elif n[x]=='3':n[x]='4'
    elif n[x]=='4':n[x]='5'
    elif n[x]=='5':n[x]='6'
    elif n[x]=='6':n[x]='7'
    elif n[x]=='7':n[x]='8'
    elif n[x]=='8':n[x]='9'
    elif n[x]=='9':
         n[x]='0'
         plus(n,x-1)
def pm(n,x):
    if n[x]=='0':
        n[x]='9'
        pm(n,x-1)
    elif n[x]=='1':n[x]='0'
    elif n[x]=='2':n[x]='1'
    elif n[x]=='3':n[x]='2'
    elif n[x]=='4':n[x]='3'
    elif n[x]=='5':n[x]='4'
    elif n[x]=='6':n[x]='5'
    elif n[x]=='7':n[x]='6'
    elif n[x]=='8':n[x]='7'
    elif n[x]=='9':
         n[x]='8'
n=list(input())
d=['0']+n
x=len(d)-1
if n[0]=='-':
    d=n[1:]
    x=len(d)-1
    pm(d,x)
    print ('-', end ='')
else:
    plus(d,x)
p =0
if d[0]=='0':
    p=1
for t in range (p,len(d)):
    print (d[t] , end='')

