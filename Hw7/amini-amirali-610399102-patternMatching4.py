n=input()
be = input()
t=0
for i in range(len(n)-len(be)+1):
    if n[i]==be[0]:
        if n[i:i+len(be)]==be:
            print ('Yes')
            t=1
            break
if t==0:
    print ('No')