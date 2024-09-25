def counter(x,y):
    d=0
    for i in x :
        if i == y :d+=1
    return d 
input()
n=input ().split()
j=counter(n,n[0])
print (j,end=" ")
for i in range(1,len(n)) :
    if n[i]==n[i-1]:
        print (j,end=' ')
    else :
        j=counter(n,n[i])
        print (j,end=" ")
