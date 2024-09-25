n=int(input())
ls=[n]*(2*n-1)
lss=[]
for z in range (1,n+1):
    for i in ls:
        print (i,end='')
    lss.append(tuple( ls))
    print ()
    for q in range (z,2*n-1-z):
        ls[q]-=1
for i in range(len(lss)-2,-1,-1):
    for j in lss[i]:
        print (j,end='')
    print ()