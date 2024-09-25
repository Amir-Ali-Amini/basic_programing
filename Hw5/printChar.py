n = input ().strip()
a=[]
l=[]
t=[]
for x in n:
    if (ord(x)>=ord('a'))&(ord(x)<=ord('z')):a.append(x)
    elif (ord(x)>=ord('A'))&(ord(x)<=ord('Z')):a.append(x)
    elif (ord(x)<=ord('9'))&(ord(x)>=ord('0')):l.append(x)
    else :t.append(x)
for q in a:
    print (q,end='')
print('')
for  z in l:
    print (z,end='')
print('')
for w in t:
    print (w,end='')