def sum(x):
    c=0
    while x>0:
        c+=x%10
        x=x//10
    if c//10==0: print (c)
    else : return sum(c)
sum(int(input()))
