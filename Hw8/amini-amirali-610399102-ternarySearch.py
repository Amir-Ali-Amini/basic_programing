st=list (map(int,input().split()))
n=int(input ())
for i in range (len(st)):
    if st[i]==n :
        print (i)
        break
else : print ('NF')