n=int(input())
if n ==0 :
    print(0)
c=""
while n>0:
    c+=str(n%8)
    n=n//8
print (c)