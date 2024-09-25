q,p=input().split()
o=e=z=0
for x in p:
    x=int(x)
    if z%2==0:
        e=e*10 + x
    else: o=10*o +x
    z+=1
w=e+o*int(q)
print (w)