from random import *
n=int(input())
max=random()
max=int(max)
t=min=max
s=t
for _ in range (n-2 ):
    t=random()
    if (max<t):max=t 
    if min>t:min=t
    s+=t
print (max, ((s/n)//0.0001)*0.0001)